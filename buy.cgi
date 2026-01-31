sub BUY {

	if($in{'no'} eq ""){&ERR("NO:가 입력되지 않았습니다.");}
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN($kpos);
	&COUNTRY_DATA_OPEN($kcon);

	&HEADER;
	$no = $in{'no'} + 1;

	$get_sol1 = $kgold;
	$get_sol2 = $krice;

	if($kskill =~ /Ab/){
	if($get_sol1 > 200000){
		$get_sol1 = 200000;
	}
	if($get_sol2 > 200000){
		$get_sol2 = 200000;
	}
	$max = 200000;
	}else{
	if($get_sol1 > 200000){
		$get_sol1 = 200000;
	}
	if($get_sol2 > 200000){
		$get_sol2 = 200000;
	}
	$max = 200000;
	}


	foreach(@no){
		$no_list .= "<input type=hidden name=no value=$_>"
	}

	$sou1 = $zsouba*100;
	$sou2 = int((2.0-$zsouba)*100);


	print <<"EOM";
<STYLE>BODY {
	CURSOR: url('samnet.cur')
}
A {
	CURSOR: url('samnet.ani'); TEXT-DECORATION: none
}
</STYLE>
<BODY oncontextmenu="return false" onselectstart="return false" ondragstart="return false" bgcolor="black" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0">
<table align="center" width="950">
    <tr>
        <td>
            <img src="$IMG/up.gif">
        </td>
    </tr>
    <tr height="600">
        <td background="$IMG/backg.gif">
<table align="center" border="1" cellspacing="0" width="752" height="492" bordercolordark="white" bordercolorlight="black">
    <tr>
        <td width="1101" height="492" background="$IMG/cola.jpg">
            <table cellpadding="0" cellspacing="0" width="752" height="488" bordercolordark="white" bordercolorlight="black">
                <tr>
                    <td width="752" height="22" colspan="8">
                        <p>&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td width="11" height="467" rowspan="6">
                        <p>&nbsp;</p>
                    </td>
                    <td width="52" height="236" rowspan="4">
                        <p>&nbsp;</p>
                    </td>
                    <td width="141" height="236" rowspan="4">
                        <table cellpadding="0" cellspacing="0">
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$cou_name[$kcon]국</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$kstr</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$kint</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$klea</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$kcha</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$kgold괴</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$krice석</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$kcex</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$ksol명</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$kgat</span></font></p>
                                </td>
                            </tr>
                        </table>

                    </td>
                    <td width="32" height="236" rowspan="4">
                    </td>
                    <td width="68" height="34">
                    </td>
                    <td width="27" height="236" rowspan="4">
	                    </td>
                    <td width="421" height="467" rowspan="6">
<center>
            <table align="center" border="1" cellspacing="0" width="371" bordercolordark="white" bordercolorlight="black" height="200">
                <tr>

                    <td width="365" height="200" background="$IMG/buy.gif">
                        <table align="center" cellpadding="0" cellspacing="0" width="344">
                            <tr>
                                <td width="97" height="178">
                                </td>
                                <td width="247" height="178">
                                    <p align="left"><font color="white" face="돋움"><span style="font-size:9pt;">어서 오십시오.<BR>여기는 쌀과 돈을 교환하는 장소입니다.<BR>현재의 시세는<BR>
쌀 100에 대해서 금 </span><font color=red><span style="font-size:9pt;">$sou1</span></font><span style="font-size:9pt;">이고<BR>
금 100에 대해서 쌀 </span><font color=red><span style="font-size:9pt;">$sou2</span></font><span style="font-size:9pt;">입니다.<BR>

그리고 또한<BR>1회의 거래로 매매할 수 있는 것은 최대로 $max 까지입니다.<BR>얼마나 교환하시겠습니까?</span></font></td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>

                    <td width="365" height="134">
<center><br><form action="$COMMAND" method="POST"><B>[쌀을 판다]</B><BR>
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
쌀 <input type=text name=num value=$get_sol2 size=4>
$no_list
<input type=hidden name=mode value=19>
<input type=hidden name=type value=1>
<input type=submit value="쌀을 판다"></form>
                                                                <p><B>[금을 판다]</B><BR>
<form action="$COMMAND" method="POST">
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
금 <input type=text name=num value=$get_sol1 size=4>
$no_list
<input type=hidden name=mode value=19>
<input type=hidden name=type value=0>
<input type=submit value="금을 판다"></form>


<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="돌아온다"></form></CENTER>
                    </td>
                </tr>
            </table>
                </center>            </center>        
                    </td>
                    <td width="8" height="467" rowspan="6">
                    </td>
                </tr>
                <tr>
                    <td width="68" height="82">
                        <p><img src="$IMG/$kchara.gif" width="64" height="80" border="0"></p>
                    </td>
                </tr>
                <tr>
                    <td width="68" height="37">
                        <p align="center"><font color="white" face="돋움"><span style="font-size:9pt;">$kname</span></font></p>
                    </td>
                </tr>
                <tr>
                    <td width="68" height="83">
                    </td>
                </tr>
                <tr>
                    <td width="312" height="35" colspan="5">
                    </td>
                </tr>
                <tr>
                    <td width="285" height="196" colspan="4">
<font color="white" face="돋움"><span style="font-size:9pt;">쌀과 금을 서로 팔아 교환합니다.<br>시세에 따라 변동률이 있으니 주의하시기 바랍니다.</span></font></td>
                    <td width="27" height="196">
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
        </td>
    </tr>
    <tr>
        <td>
            <img src="$IMG/down.gif">
        </td>
    </tr>
</table>
EOM

	&FOOTER;

	exit;

}
1;