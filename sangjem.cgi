sub SANGJEM {

	if($in{'no'} eq ""){&ERR("NO:가 입력되지 않습니다.");}
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&TIME_DATA;
	open(IN,"$ARM_LIST");
	@ARM_DATA = <IN>;
	close(IN);
	($armname,$armval,$armstr,$armlea,$armint,$armcha,$armclass,$armtownid,$armname1) = split(/<>/,$ARM_DATA[$karm]);
	$armval = ($armval * 0.6);
	if($kvsub2 eq 0){$armval = int($armval / 10);}
	&HEADER;
	$no = $in{'no'} + 1;

	foreach(@no){
		$no_list .= "<input type=hidden name=no value=$_>"
	}

	$get_sol = $klea - $ksol;
	print <<"EOM";
<STYLE>BODY {
	CURSOR: url('samnet.cur')
}
A {
	CURSOR: url('samnet.ani'); TEXT-DECORATION: none
}
</STYLE>
<BODY oncontextmenu="return false" onselectstart="return false" ondragstart="return false">
<body leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" text="white">
<table align="center" width="950">
    <tr>
        <td>
            <img src="$IMG/up.gif">
        </td>
    </tr>
    <tr height="500">
        <td background="$IMG/backg.gif">
            <table align="center" cellpadding="0" cellspacing="0" width="752" height="400">
                <tr>
                    <td width="934" background="$IMG/sangj1.jpg">
                        <table cellpadding="0" cellspacing="0" width="100%">
                            <tr>
                                <td width="742" height="61" colspan="2">
                                    <p>&nbsp;</p>
                                </td>
                            </tr>
                            <tr>
                                <td width="200" height="82">
                                    <p>&nbsp;</p>
                                </td>
                                <td width="551" height="82">
                                    <p><span style="font-size:9pt;">왕서방의 아이템상점이다.<br>지금 
                                    팔고 있는 것은 장비와 복장뿐이라구..<br>뭐라고 
                                    불친절하다고?<br>시끄럽다 물건이나 
                                    사라!</span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="742" height="249" colspan="2">
<table align="center" cellpadding="0" cellspacing="0">
    <tr>
        <td>
<form action="./command.cgi" method="post" style="margin:0;padding:0;">
$no_list
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=15>
<input type=image src="$IMG/sangj2.jpg">
</form>
        </td>
        <td>
<form action="./command.cgi" method="post" style="margin:0;padding:0;">
$no_list
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=16>
<input type=image src="$IMG/sangj3.jpg">
</form>
        </td>
    </tr>
</table>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
<center><form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="돌아온다"></form>
        </td>
    </tr>
    <tr>
        <td>
            <img src="$IMG/down.gif">
        </td>
    </tr>
</table>
</body>

EOM

	&FOOTER;

	exit;

}
1;