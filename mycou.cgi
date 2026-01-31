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
	open(IN,"./charalog/log/$kid.cgi");
	@LOG_DATA = <IN>;
	close(IN);
	&TOWN_DATA_OPEN($kpos);
	&COUNTRY_DATA_OPEN($kcon);


	&GWAN2;

	$p=0;
	foreach(@LOG_DATA){
		$log_list .= "<font color=navy>●</font>$LOG_DATA[$p]<BR>";$p++;
	}

	opendir(dirlist,"./charalog/main");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"./charalog/main/$file")){
				&ERR2("파일 오픈 에러!");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);

	$t_list = "<TBODY bgcolor=$ELE_C[$xele]><TR><TH width=50>도시</TH><TH width=50>농민</TH><TH width=50>농업</TH><TH width=50>상업</TH><TH width=50>성벽</TH><TH width=50>방어도</TH><TH width=50>기술력</TH><TH width=30>민심</TH><TH width=30>시세</TH><TH width=100>주둔중인 장수</TH></TR>";

	$num=0;
	foreach(@CL_DATA){
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint) = split(/<>/);
			if($xking eq $kid || $x0 eq $kid || $x1 eq $kid || $x17 eq $kid){
			$list[$epos] .= "<a href=\"javascript:info('$eid')\">$ename</a>($esol명), ";
			}else{
			$list[$epos] .= "<a href=\"javascript:info('$eid')\">$ename</a>, ";
			}
	}

	$zc=0;
	foreach(@TOWN_DATA){
		($z2name,$z2con,$z2num,$z2nou,$z2syo,$z2shiro,$z2nou_max,$z2syo_max,$z2shiro_max,$z2pri,$z2x,$z2y,$z2souba,$zdef_att,$zsub1,$zsub2)=split(/<>/);
		if($z2con eq $kcon){
		$t_list .= "<TR><Th>$z2name</Th><TD><center>$z2num</TD><TD><center>$z2nou/$z2nou_max</TD><TD><center>$z2syo/$z2syo_max</TD><TD><center>$z2shiro/$z2shiro_max</TD><TD><center>$zdef_att/1000</TD><TD><center>$zsub1/1200</TD><TD><center>$z2pri</TD><TD><center>$z2souba</TD><TD>$list[$zc]</TD></TR>";
		}
		$zc++;
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
        <td width="945" height="857" background="$IMG/backg.gif">
<CENTER>
<TABLE WIDTH="70%" height=100% cellpadding="0" cellspacing="0" border=0><tr><td align=center>
<br><B>《 $xname국의 정보 》</b>
<br>
<body bgcolor="white" text="black" link="blue" vlink="purple" alink="red">
<table align="center" border="1" cellspacing="0" width="700" bgcolor=$ELE_BG[$xele]>
    <tr>
        <td width="1101" height="795">
            <table align="center" cellpadding="0" cellspacing="0" width="684">
                <tr>
                    <td width="684" height="25" colspan="6" align="center">
                        <p align="center"><span style="font-size:9pt;"><font face="돋움">국가수뇌부</font></span></p>
                    </td>
                </tr>
                <tr>
                    <td width="684" height="113" colspan="6">
                        <table align="center" cellpadding="0" cellspacing="0" width="299">
                            <tr>
                                <td width="142">
                                    <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                                        <tr>
                                            <td width="64" height="80" background="$IMG/$king_chara.gif">
                                            </td>
                                        </tr>
                                        <tr>
                                            <td width="64" height="30">
                                                <p align="center">$king_name<br><img src="$IMG/gg01.jpg">
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                                <td width="141">
                                    <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                                        <tr>
                                            <td width="64" height="80" background="$ximg[0]">
                                            </td>
                                        </tr>
                                        <tr>
                                            <td width="64" height="30">
                                                <p align="center">$tname[0]<br><img src="$IMG/gg02.jpg">
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td width="50%" height="25" colspan="3">
                        <p align="center"><font face="돋움"><span style="font-size:9pt;">장군관직</span></font></p>
                    </td>
                    <td width="50%" height="25" colspan="3">
                        <p align="center"><font face="돋움"><span style="font-size:9pt;">문관관직</span></font></p>
                    </td>
                </tr>
                <tr>
                    <td width="50%" height="108" colspan="3">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[1]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[1]<br><img src="$IMG/gg03.jpg"></p>
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="50%" height="108" colspan="3">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[17]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[17]<br><img src="$IMG/gg04.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[2]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[2]<br><img src="$IMG/gg05.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[3]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[3]<br><img src="$IMG/gg06.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[4]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[4]<br><img src="$IMG/gg07.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[18]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[18]<br><img src="$IMG/gg20.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[19]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[19]<br><img src="$IMG/gg21.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[20]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[20]<br><img src="$IMG/gg22.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[5]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[5]<br><img src="$IMG/gg08.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[9]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[9]<br><img src="$IMG/gg12.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[13]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[13]<br><img src="$IMG/gg16.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[21]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[21]<br><img src="$IMG/gg23.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[23]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[23]<br><img src="$IMG/gg25.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[25]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[25]<br><img src="$IMG/gg27.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[6]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[6]<br><img src="$IMG/gg09.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[10]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[10]<br><img src="$IMG/gg13.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[14]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[14]<br><img src="$IMG/gg17.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[22]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[22]<br><img src="$IMG/gg24.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[24]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[24]<br><img src="$IMG/gg26.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[26]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[26]<br><img src="$IMG/gg28.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[7]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[7]<br><img src="$IMG/gg10.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[11]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[11]<br><img src="$IMG/gg14.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[15]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[15]<br><img src="$IMG/gg18.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <p align="center"></td>
                    <td width="16%" height="130">
                        <p align="center"></td>
                    <td width="16%" height="130">
                        <p align="center"></td>
                </tr>
                <tr>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[8]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[8]<br><img src="$IMG/gg11.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[12]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[12]<br><img src="$IMG/gg15.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="64" height="80" background="$ximg[16]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[16]<br><img src="$IMG/gg19.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                    </td>
                    <td width="16%" height="130">
                    </td>
                    <td width="16%" height="130">
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
<br>
<TABLE border=0 cellspacing=1 bgcolor=$TABLE_C>
    <TBODY bgcolor=FFFFFF>
$t_list
</TBODY></TABLE>
</body>

<br>
<TABLE border=0 cellspacing=1>
    <TBODY>
          <TR>
<TD>
<form action=\"$FILE_STATUS\" method=\"post\"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=STATUS><input type=submit value=\"돌아온다\"></form>
</TD></TR>
</TBODY></TABLE>


</TD></TR>
</TBODY></TABLE>
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

