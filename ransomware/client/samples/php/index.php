<?
/*-----------------------------------------------------------------------------------------------------
AUTHOR: Joshua Malan
COMPANY: TeksFX
WEBSITE: www.teksfx.com
EMAIL: jmalan@teksfx.com
 
    Password Structure Validation:
     
        $passVer = the password
        $symbolErrors:
            If there is an error with invalid symbols it will return the details of 
            that error in a bullited list <ul>
        $results:
            If the password does not meet the spefications it will return an ordered 
            list <ol> with the description of why it did not meet the specifications.
             
-----------------------------------------------------------------------------------------------------*/
function checkPassword($passVer){
    global $symbolErrors;
    global $results;
    $invalid_symbols = array(0 => "$",1 => "%",2 => "&");
    $valid_symbols = array(0 => "!",1 => "@",2 => "#",3 => "^",4 => "*",5 => "(",6 => ")",7 => "-",
                    8 => "_",9 => "=",10 => "+",11 => "[",12 => "]",13 => "{",14 => "}",15 => ";",
                    16 => ":",17 => ",",18 => "<",19 => ">",20 => ".",21 => "/",22 => "~");
    $length = strlen($passVer);    
    if ($length >= 6){
        $lengthVerified = true;
    } else {
        $lengthVerified = false;
    }
     
    for($i=0;$i<$length;$i++){
        $chars[] = substr($passVer, $i, 1);
    }
    $symbolErrors = "<ul>";
        while(list($key,$val) = each($chars)){
            if (in_array($val,$invalid_symbols)){
                $symbolErrors .= "<li><span class='defaultBoldRed'>$val</span> is an invalid symbol.</li>";
                $invalidSymbol = true;
            }
            if (in_array($val,$valid_symbols)){
                $validSymbol = true;
            }
            if (ereg('[0-9]', $val)){
                $numericVerified = true;
            }
            if(ereg('[A-Z]', $val)){
                $alphaUpVerified = true;
            }
            if(ereg('[a-z]', $val)){
                $alphaLowVerified = true;
            }
        }
    $symbolErrors .= "</ul>";
     
    $results = "<ol>";
        if ($lengthVerified == true){
            //$results .= "<span class='defaultGreen'>The length check passed</span><br>";
        } else {
            $results .= "<li><span class='defaultRed'>The length check failed, your password needs to be 6 characters or more.</span><br></li>";
        }
         
        if ($invalidSymbol != true){
            //$results .= "<span class='defaultGreen'>The invalid symbol check passed</span><br>";
        } else {
            $results .= "<li><span class='defaultRed'>The invalid symbol check failed and are mentioned above.</span><br></li>";
        }
         
        if ($validSymbol == true){
            //$results .= "<span class='defaultGreen'>The valid symbol check passed</span><br>";
        } else {
            $results .= "<li><span class='defaultRed'>The valid symbol check failed. You need to have a symbol in your password other than $ % or &amp;.</span><br></li>";
        }
         
        if ($numericVerified == true){
            //$results .= "<span class='defaultGreen'>The numeric check passed</span><br>";
        } else {
            $results .= "<li><span class='defaultRed'>The numeric check failed because you need to have a number in your password.</span><br></li>";
        }
         
        if ($alphaUpVerified == true){
            //$results .= "<span class='defaultGreen'>The alpha upper case check passed</span><br>";
        } else {
            $results .= "<li><span class='defaultRed'>The alpha upper case check failed because you need to have one of the letters capitalized.</span><br></li>";
        }
         
        if ($alphaLowVerified == true){
            //$results .= "<span class='defaultGreen'>The alpha lower case check passed</span><br>";
        } else {
            $results .= "<li><span class='defaultRed'>The alpha lower case check failed because you need a lower case letter.</span><br></li>";
        }
    $results .= "</ol>";
}
 
echo"<html>
<head>
    <title>Change Password</title>
    <style>
        .default{font:9pt Arial,Helvetica,Veranda;color:#000000;}
        .defaultWhite{font:9pt Arial,Helvetica,Veranda;color:#FFFFFF;}
        .defaultRed{font:9pt Arial,Helvetica,Veranda;color:#D60000;}
        .defaultBlack{font:9pt Arial,Helvetica,Veranda;color:#000000;}
        .defaultBlue{font:9pt Arial,Helvetica,Veranda;color:#00529C;}
        .defaultGreen{font:9pt Arial,Helvetica,Veranda;color:#006600;}
        .defaultOrange{font:9pt Arial,Helvetica,Veranda;color:#DC9306;}
        .defaultBold{font:bold 9pt Arial,Helvetica,Veranda;color:#000000;}
        .defaultBoldWhite{font:bold 9pt Arial,Helvetica,Veranda;color:#FFFFFF;}
        .defaultBoldBlack{font:bold 9pt Arial,Helvetica,Veranda;color:#000000;}
        .defaultBoldYellow{font:bold 9pt Arial,Helvetica,Veranda;color:#D60000;}
        .defaultBoldBlue{font:bold 9pt Arial,Helvetica,Veranda;color:#00529C;}
        .defaultBoldLtBlue{font:bold 9pt Arial,Helvetica,Veranda;color:#EDEFF3;}
        .defaultBoldRed{font:bold 9pt Arial,Helvetica,Veranda;color:#D60000;}
        .defaultBoldGreen{font:bold 9pt Arial,Helvetica,Veranda;color:#006600;}
        .defaultBoldOrange{font:bold 9pt Arial,Helvetica,Veranda;color:#DC9306;}
        .defaultBoldGrey{font:bold 9pt Arial,Helvetica,Veranda;color:#888888;}
    </style>
</head>
 
<body $body>
<form><P>&nbsp;</P>
    <table border='0' cellpadding='1' cellspacing='0' width='400' align='center' bgcolor='#000000'><tr><td>
        <table border='0' cellpadding='2' cellspacing='0' width='400' align='center' bgcolor='#FFFFFF'>
            <tr class='highlight'>
                <td align='center' class='defaultBoldWhite' bgcolor='#00529C'>Please change your password in the box below.</td>
            </tr>
            <tr class='noHighlight'>
                <td align='center'>
                    <input type='text' name='passVer' value='$passVer' class='defaultBlue'>
                    <input type='submit' value='CHANGE' class='defaultBoldBlue'>
                </td>
            </tr>
            <tr class='highlight'>
                <td class='defaultBold'>
                <P align='center'>Below is the description of the problem with your password.</P>
                ";
                if (isset($passVer)){
                    checkPassword($passVer);
                    if ($symbolErrors != "<ul></ul>" || $results != "<ol></ol>"){
                        echo $symbolErrors;
                        echo $results;
                    } else {
                        //YOUR UPDATE STATEMENT HERE
                        echo "<center><span class='defaultBoldRed'>Your password acceptable, <a href='../index.html'>Click Here</a> to continue.</span></center>";
                    }            
                }
                 
                echo"
                </td>
            </tr>
        </table>
    </td></tr></table>
</form>
</body>
</html>";
?>