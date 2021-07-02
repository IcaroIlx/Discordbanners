<?php

$nome = $_POST['token'];
$filtro = array('&', '|', '>', '<', '/', '?', '"');
$sub = str_replace($filtro, '', $nome);


$token = $_POST['token'];
$filename = 'Imagens/'.$sub.'.txt';


$file = $_FILES['bannerup'] ['name'];
$_UP ['pasta'] = 'Imagens/';
$_UP{'formato'} = array('png', 'gif', 'jpg', 'wepb');
$_UP{'renomear'} = true;
$_UP['erros'] [0] = 'sucesso';
$_UP['erros'] [1] = 'erro';

if($_FILES['bannerup'] ['erro'] != 0) {
    die("erro". $_UP['erros'][$_FILES['bannerup']['erro']]);
        exit;
    }
    $exte = strtolower(end(explode('.', $_FILES['bannerup']['name'])));
        if(array_search($exte, $_UP['formato']) === false){
            echo "formato de imagem nao compativel";
        }else{
            if($_UP['renomear'] == true){
                $rem = $sub.'.gif';
            }
        }if(move_uploaded_file($_FILES['bannerup']['tmp_name'], $_UP['pasta']. $rem)){
            $img = file_get_contents("Imagens/".$sub.".gif");
            $convert = base64_encode($img);
            $fileopen = fopen($filename,"wb");
            fwrite($fileopen, $convert);
            fclose($fileopen);
            $fps = "python3 fap.py " .$sub. " " .$sub. ".txt";
            $output = shell_exec($fps);
            header('location: sucesso/index.html');; 
        }else{
            header('location: erro/index.html');
        }
?>
