#!C:\xampp\perl\bin\perl.exe

use lib 'C:/xampp/htdocs';
require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

if($MENTE) { &ERR("로딩중입니다. 잠시만 기다려 주십시오."); }
&DECODE;
&BONG3;


sub BONG3 {

	&CHARA_MAIN_OPEN;
	open(IN,"./charalog/log/$kid.cgi");
	@LOG_DATA = <IN>;
	close(IN);
	&TOWN_DATA_OPEN($kpos);
	&COUNTRY_DATA_OPEN($kcon);


	&GWAN2;

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

	
	$num=0;
	foreach(@TOWN_DATA){
		($zzname,$zzcon,$zznum,$zznou,$zzsyo,$zzshiro,$zznou_max,$zzsyo_max,$zzshiro_max,$zzpri,$zzx,$zzy,$zzsouba,$zzdef_att,$zzsub1,$zzsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zzname1,$zzname2,$zzbong1,$zzbong2,$zzbong3)=split(/<>/);
		if($kpos eq $num){
		$bongid1 = "$zzbong1";
		$bongid2 = "$zzbong2";
		$bongid3 = "$zzbong3";
		}
		$num++;
	}

	foreach(@CL_DATA) {
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/);
		if("$bongid1" eq "$eid"){
			$jjang1 = "$ename";
			$jjan1 = "$emes";
			$jja1 = "$echara";
		}
		if("$bongid2" eq "$eid"){
			$jjang2 = "$ename";
			$jjan2 = "$emes";
			$jja2 = "$echara";
		}
		if("$bongid3" eq "$eid"){
			$jjang3 = "$ename";
			$jjan3 = "$emes";
			$jja3 = "$echara";
		}
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
        <td width="945" height="787" background="$IMG/backg.gif">
            <table align="center" cellpadding="0" cellspacing="0" width="700">
                <tr>
                    <td width="940">
                        <p><img src="$IMG/law1.gif" width="700" height="22" border="0"></p>
                    </td>
                </tr>
                <tr>
                    <td width="940" height="681" background="$IMG/law3.gif">
                        <table valign="up" align="center" cellpadding="0" cellspacing="0" bgcolor="black" width="94%">
                            <tr>
                                <td width="654" height="100">
                                    <p><span style="font-size:9pt;"><b>$zname성의 
                                    봉토일람</b><br>$zname성에 입주해있는 영주들의 봉토게시판을 일람합니다.<br>해당 봉토게시판에 글을 남길 경우 해당 영주들에게 공헌치 +8씩 적립됩니다.<br>단, 해당 영주가 자신의 봉토에 글을 써도 공헌치는 받을 수 없습니다.<br>아래에 
                                    들어가시고자 하는 봉토게시판을 선택해주십시오.</span></p>
                                </td>
                            </tr>
                        </table>
			<br>
                        <table align="center" border="5" cellspacing="0" width="649" height="411" bordercolordark="black" bordercolorlight="black">
                            <tr>
                                <td width="649" height="440" background="$IMG/bongtoi.jpg">
                                    <table cellpadding="0" cellspacing="0" width="645" height="411">
                                        <tr>
                                            <td width="85" height="439" rowspan="6">
                                            </td>
                                            <td width="108" height="24">
                                            </td>
                                            <td width="213" height="24" colspan="2">
                                            </td>
                                            <td width="239" height="24" colspan="2">
                                            </td>
                                        </tr>
                                        <tr>
                                            <td width="108" height="101">
                        <table align="center" width="80" cellpadding="0" cellspacing="0">
                            <tr>
                                <td width="136" height="82">
                                    <table align="center" border="2" cellspacing="0" width="64" height="80" bordercolordark="black" bordercolorlight="black">
                                        <tr>
                                            <td width="64" height="80" background="$IMG/$jja1.gif">
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <tr><form action=\"./mydata\.cgi" method=\"post\">
                                <td width="136" align="center">
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=BONGTOG><input type=hidden name=bongid value=$bongid1><input type=hidden name=bongtown value=$zname><input type=hidden name=bongname value=$jjang1><input type=hidden name=bongimg value=$jja1><input type=submit value=\"$jjang1\">
                                </td>
				</form>
                            </tr>
                        </table>
                                            </td>
                                            <td width="213" height="101" colspan="2">
                                            </td>
                                            <td width="110" height="101">
                        <table align="center" width="80" cellpadding="0" cellspacing="0">
                            <tr>
                                <td width="136" height="82">
                                    <table align="center" border="2" cellspacing="0" width="64" height="80" bordercolordark="black" bordercolorlight="black">
                                        <tr>
                                            <td width="64" height="80" background="$IMG/$jja2.gif">
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <tr><form action=\"./mydata\.cgi" method=\"post\">
                                <td width="136" align="center">
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=BONGTOG><input type=hidden name=bongid value=$bongid2><input type=hidden name=bongtown value=$zname><input type=hidden name=bongname value=$jjang2><input type=hidden name=bongimg value=$jja2><input type=submit value=\"$jjang2\">
                                </td>
				</form>
                            </tr>
                        </table>
                                            </td>
                                            <td width="129" height="101">
                                            </td>
                                        </tr>
                                        <tr>
                                            <td width="560" height="15" colspan="5">
                                            </td>
                                        </tr>
                                        <tr>
                                            <td width="108" height="266" rowspan="3">
                                            </td>
                                            <td width="108" height="276" rowspan="3">
                                            </td>
                                            <td width="105" height="117">
                                            </td>
                                            <td width="239" height="266" rowspan="3" colspan="2">
&nbsp;                                            </td>
                                        </tr>
                                        <tr>
                                            <td width="105" height="112">
                        <table align="center" width="80" cellpadding="0" cellspacing="0">
                            <tr>
                                <td width="136" height="82">
                                    <table align="center" border="2" cellspacing="0" width="64" height="80" bordercolordark="black" bordercolorlight="black">
                                        <tr>
                                            <td width="64" height="80" background="$IMG/$jja3.gif">
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <tr><form action=\"./mydata\.cgi" method=\"post\">
                                <td width="136" align="center">
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=BONGTOG><input type=hidden name=bongid value=$bongid3><input type=hidden name=bongtown value=$zname><input type=hidden name=bongname value=$jjang3><input type=hidden name=bongimg value=$jja3><input type=submit value=\"$jjang3\">
                                </td>
				</form>
                            </tr>
                        </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td width="105" height="39">
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>
<form action=\"$FILE_STATUS\" method=\"post\">
                <p align="center"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=STATUS><input type=submit value=\"돌아온다\"></form>
                    </td>
                </tr>
                <tr>
                    <td width="940">
                        <p><img src="$IMG/law2.gif" width="700" height="22" border="0"></p>
                    </td>
                </tr>
            </table>
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