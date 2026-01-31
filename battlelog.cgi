#!C:\xampp\perl\bin\perl.exe

use lib 'C:/xampp/htdocs';
require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

if($MENTE) { &ERR("로딩중입니다. 잠시만 기다려 주십시오."); }
&DECODE;
&TOP;

sub TOP {

	&CHARA_MAIN_OPEN;
	open(IN,"./log_file/battle_log.cgi");
	@BATTLE_DATA = <IN>;
	close(IN);

	$p=0;
	foreach(@BATTLE_DATA){
		$battle_list .= "$BATTLE_DATA[$p]<BR>";$p++;
	}

	&HEADER;
	print <<"EOM";
<body bgcolor="white" text="white" link="blue" vlink="purple" alink="red" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0">
<table align="center" cellpadding="0" cellspacing="0" width="945">
    <tr>
        <td width="945">
            <p><img src="$IMG/up.gif" width="950" height="93" border="0"></p>
        </td>
    </tr>
    <tr>
        <td width="945" height="857" background="$IMG/backg.gif"><br>
            <table align="center" cellpadding="0" cellspacing="0" width="700">
                <tr>
                    <td width="940">
                        <p><img src="$IMG/law1.gif" width="700" height="22" border="0"></p>
                    </td>
                </tr>
                <tr>
                    <td width="940" height="785" background="$IMG/law3.gif">
<CENTER>
<br>
<TABLE WIDTH="95%" height=100% cellpadding="0" cellspacing="0" border=0><tr><td valign="up">
$battle_list
<br>
<p align="center"><form action=\"$FILE_STATUS\" method=\"post\"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=STATUS><input type=submit value=\"돌아온다\"></p>
</form>

</TD></TR>
</TBODY></TABLE><br></center>                    </td>
                </tr>
                <tr>
                    <td width="940">
                        <p><img src="$IMG/law2.gif" width="700" height="22" border="0"></p>
                    </td>
                </tr>
            </table><br>
        </td>
    </tr>
    <tr>
        <td width="945">
            <p><img src="$IMG/down.gif" width="950" height="26" border="0"></p>
        </td>
    </tr>
</table>
</body>

EOM

	&FOOTER;
	exit;

}
