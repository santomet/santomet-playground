<?php
#echo 'Hello ' . htmlspecialchars($_GET["name"]) . '!';
#htmlspecialchars($_GET["c"])

function redirect($url, $statusCode = 303)
{
   header('Location: ' . $url, true, $statusCode);
   die();
}


$channel = "1";
$redirect = false;

if (isset($_GET["c"]))
    $channel = htmlspecialchars($_GET["c"]);

if (isset($_GET["r"]) and htmlspecialchars($_GET["r"]) == "true")
    $redirect = true;

$url = "http://www.rtvs.sk/json/live5.json?c=" . $channel . "&b=chrome&p=linux&v=64&f=0&d=1";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true );
// This is what solved the issue (Accepting gzip encoding)
curl_setopt($ch, CURLOPT_ENCODING, "gzip,deflate");     
$response = curl_exec($ch);
curl_close($ch);
#echo $response;
#echo "HELLO\n";

$arr = json_decode($response);
$url_m3u8 = $arr[0]->{"sources"}[0]->{"file"};
$strpos = strrpos($url_m3u8, "/");
$url_base = substr($url_m3u8, 0, $strpos+1);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url_m3u8);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true );
// This is what solved the issue (Accepting gzip encoding)
curl_setopt($ch, CURLOPT_ENCODING, "gzip,deflate");     
$response = curl_exec($ch);

$lines = explode("\n", $response);

$finalurl = $url_base . $lines[5];

if ($redirect)
    redirect($finalurl);
else
    echo $url_base . $lines[5];

?>
