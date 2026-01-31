
sub KING_COM7 {


	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN("$kcon");
	&TIME_DATA;



	$xch = "$in{'chx'}";

	$xsub = "$x0,$x1,$x2,$x3,$x4,$x5,$x6,$x7,$x8,$x9,$x10,$x11,$x12,$x13,$x14,$x15,$x16,$x17,$x18,$x19,$x20,$x21,$x22,$x23,$x24,$x25,$x26,$xxsub1,$xxsub2,";

	&COUNTRY_DATA_INPUT;
	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>자국 IRC의 채널제목을 #$in{'chx'}로 설정했습니다.</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="확인"></form></CENTER>
EOM

	&FOOTER;

	exit;

}
1;