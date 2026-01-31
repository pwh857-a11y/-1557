sub DEF_BUY {

	if($in{'no'} eq ""){&ERR("NO:가 입력되지 않았습니다.");}
	&CHARA_MAIN_OPEN;
	&CHARA_ITEM_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&TIME_DATA;

	open(IN,"$PRO_LIST");
	@PRO_DATA = <IN>;
	close(IN);
	($proname,$proval,$prostr,$prolea,$proint,$procha,$proclass,$protownid) = split(/<>/,$PRO_DATA[$kbook]);
	$proval = int($proval * 0.6);
	if($kvsub2 eq 0){$proval = int($proval / 10);}
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
<body bgcolor="white" text="white" link="blue" vlink="purple" alink="red" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0">
<table align="center" cellpadding="0" cellspacing="0" width="945">
    <tr>
        <td width="945">
            <p><img src="$IMG/up.gif" width="950" height="93" border="0"></p>
        </td>
    </tr>
    <tr>
        <td width="945" height="300" background="$IMG/backg.gif"><br>
<table align="center" cellpadding="0" cellspacing="0" width="700" height="186" background="$IMG/item1.jpg">
    <tr>
        <td width="805">
            <table cellpadding="10" cellspacing="0" width="700">
                <tr>
                    <td width="180" height="185" rowspan="2">
                    </td>
                    <td width="480" height="63">
                        <p align="right"><span style="filter:shadow(color=#BLACK,direction=135); color:FFFFFF; font-size:36px; height:1pt;">왕서방의 
                        복장상점</span></p>
                    </td>
                </tr>
                <tr>
                    <td width="480" height="122" valign="up">
                        <p align="left"><span style="font-size:9pt;"><font color=black>흐음 $kname, 자넨가?<br>귀찮게 왜 또 왔는가?<br>짜증이 
                        난다네<BR>복장을 살려고 말인가?<BR>현재 자네가 팔려고 
                        하는 $proname의 가격은 금 </span><FONT color=red><span style="font-size:9pt;">$proval</span></FONT><span style="font-size:9pt;"> 이라네.<BR>아래에 
                        팔고 있는 아이템의 
리스트들을 보게나.</font></span></td>
                </tr>
            </table>
        </td>
    </tr>
</table>
<br>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<center><TABLE bgcolor=$TABLE_C>

EOM

	open(IN,"$PRO_LIST") or &ERR('파일을 열지 않았습니다.');
	@PRO_DATA = <IN>;
	close(IN);

	$list = "<TR align=center><TD bgcolor=$TD_C1>선택</TD><TD bgcolor=$TD_C2 width=80>명칭</TD><TD align=right bgcolor=$TD_C3>가격</TD><TD bgcolor=$TD_C2 width=40>무력</TD><TD bgcolor=$TD_C2>통솔력</TD><TD bgcolor=$TD_C2 width=40>지력</TD><TD bgcolor=$TD_C2 width=40>매력</TD><TD bgcolor=$TD_C2 width=360>복장효과</TD></TR>";
	$s_i=0;
	foreach(@PRO_DATA){
		($proname,$proval,$prostr,$prolea,$proint,$procha,$proclass,$protownid,$proname1) = split(/<>/);
		if($kvsub2 eq 0){$proval = int($proval / 10);}
		if($protownid eq 0){
			$list .= "<TR align=center><TD bgcolor=$TD_C1><input type=radio name=select value=$s_i></TD><TD bgcolor=$TD_C2>$proname</TD><TD align=right bgcolor=$TD_C3>금 $proval</TD><TD bgcolor=$TD_C2>$prostr</TD><TD bgcolor=$TD_C2>$prolea</TD><TD bgcolor=$TD_C2>$proint</TD><TD bgcolor=$TD_C2>$procha</TD><TD bgcolor=$TD_C2>$proname1</TD></TR>";
		}
		$s_i++;
	}


print <<"EOM";
$list

</TABLE>
$no_list
<br>
<table align="center">
    <tr>
        <td>
<input type=hidden name=mode value=23>
<input type=submit value="구입한다"></form>
        </td>
        <td>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="돌아온다"></form>
        </td>
    </tr>
</table>
<br>
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
1;