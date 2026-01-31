sub BONGTOG_W {

	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN("$kcon");
	$sno = $kclass / 500;
	if($sno > 43){$sno = 43;}

	open(IN,"./charalog/per/$in{'bongid'}\.cgi") or &ERR('봉토가 없습니다.');
	@BBS_DATA = <IN>;
	close(IN);


	&HEADER;

	print <<"EOM";
<STYLE>BODY {
	CURSOR: url('samnet.cur')
}
A {
	CURSOR: url('samnet.ani'); TEXT-DECORATION: none
}
</STYLE>
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
				<table cellpadding="0" cellspacing="0"><tr><td width="$kstr1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kstr</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
				<table cellpadding="0" cellspacing="0"><tr><td width="$kint1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kint</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
				<table cellpadding="0" cellspacing="0"><tr><td width="$klea1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$klea</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$kcha1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kcha</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$kgold1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kgold</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$krice1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$krice</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$kcex1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kcex</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$ksol1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$ksol</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$kgat" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kgat</span></font></td></tr></table>
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
		    <form action="./mydata.cgi" method="post">
                        <table border="1" align="center" cellspacing="0" width="400" bordercolordark="white" bordercolorlight="black">
                            <tr>
				
                                <td width="394" height="23">
                                    <p align="center"><input type=text name=title size="54"></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="394">
                                    <p align="center"><textarea name=ins cols="53" rows="20"></TEXTAREA>
                                </td>
                            </tr>
                        </table>
			<p align="center"><br><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=bongid value=$in{'bongid'}><input type=hidden name=bongname value=$in{'bongname'}><input type=hidden name=bongimg value=$in{'bongimg'}><input type=hidden name=bongtown value=$in{'bongtown'}><input type=hidden name=mode value=BONGTOG_WRITE><input type=submit style="font-family:궁서; color:$ELE_C[$xele]; background-color:$ELE_BG[$xele]; border-width:1; border-color:black; border-style:solid;" value="게시물을 게시한다"></form>
                        <p align="center"><form action="./mydata.cgi" method="post"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=BONGTOG><input type=hidden name=bongid value=$in{'bongid'}><input type=hidden name=bongname value=$in{'bongname'}><input type=hidden name=bongtown value=$in{'bongtown'}><input type=hidden name=bongimg value=$in{'bongimg'}><input type=submit style="font-family:궁서; color:$ELE_C[$xele]; background-color:$ELE_BG[$xele]; border-width:1; border-color:black; border-style:solid;" value="게시판으로 돌아간다"></form>
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
                        <p align="center"><font color="white" face="돋움"><span style="font-size:9pt;"><a href=\"javascript:info('$kid')\">$kname</a></span></font></p>
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
                    <td width="285" height="196" colspan="4" valign="up">
<font color="white" face="돋움"><span style="font-size:9pt;">이 곳은 $in{'bongtown'}성에 위치해있는 
                        $in{'bongname'}님의 봉토게시판입니다.<br>이 곳에 글을 남겨 $in{'bongname'}님에게 
                        안부를 남기는 용도입니다.<br>재야인사, 타국의 장수들도 
                        안부를 남길 수 있습니다.<br>글을 하나 쓸 때마다 해당 영주에게 
                        공헌치 +8이 지급됩니다.<br>단, 서로 공헌치 주고받기 식의 
                        도배가 GM들에게 발각될 시 접속차단이나 영구삭제가 될 
                        수 있으니 주의해주시기 바랍니다.</span></font></td>
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