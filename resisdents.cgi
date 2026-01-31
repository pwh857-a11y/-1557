sub RESISDENTS {

	&CHARA_MAIN_OPEN;

$P_MES[0] = "어서오세요!<br>혹시 중원에는 처음 나가시는 것인지요?<br>헤헷~ 이 기본적인 게임의 개념과 흐름, 플레이어의 목적에 대해 설명해줄게요.";
$P_MES[1] = "이 게임의 목표는 군주와 부하들이 합심하여 자신의 국가를 천하통일시키는거에요.<br>엥? 그 정도는 알고 계시다구요?<br>하지만 개성적인 장수들을 통합시킨다는 건 쉬운일은 아닐꺼에요.";
$P_MES[2] = "이 게임은 2시간마다 1턴씩 갱신돼요<BR>2시간 경과하면 다음의 턴으로 진행된답니다.<br>즉 1년은 12개월이면 1년은 하루가 되는거에요.<br>즉 하루마다 1년씩 지나간다고 보면 되요.";
$P_MES[3] = "턴이 진행되면 삼모전커맨드에 지정되었던 순서대로 다음의 행동을 일으키게 된답니다.<BR>최대 24턴까지 예약이 가능하니까 행동이 멈추지 않게 하루에 한번쯤은 명령을 내려주셔야되요.<br>게임을 안하고 계속 캐릭터를 방치하면 돌연병사하게 되니 주의하시구요.";
$P_MES[4] = "초보때뿐만 아니라 건국 초기에는 내정 커맨드를 꾸준히 해주셔야 해요.<BR>내정은 나라의 근간이요! 국력이니까요..<br>싸우는 것만이 능사가 아니랍니다.<br>내정으론 상업, 농지, 성, 성방어도가 있어요.";
$P_MES[5] = "농지는 7월의 식량 수확을, 상업은 1월의 금의 수입에 영향을 끼칩니다.<BR>적국에 인접하고 있어 공격받을 것 같은 위험성이 있을시에는 성을 강화시키는 것도 좋은 방법입니다.";
$P_MES[6] = "내정이 어느 정도 탄탄하고 유능한 장수가 많다면 타국에게 전쟁을 걸어봐요!<BR>단독으로 공격하는 것보다도 자국의 사람들과 회의를 통해 발석거부대와 기병부대, 보병부대를 연계해서 공격하는 편이 효과적이랍니다.";
$P_MES[7] = "수고하셨어요. 기본적인 설명은 끝났네요.<br>사실 이건 기본적인거고 중원에서 싸우다보면 저보다도 능숙해지실거에요!";
	&HEADER;

	print <<"EOM";
<TABLE WIDTH="100%" height=100%>
<TBODY><TR>
<TD WIDTH=100% height=5> <font size=4>　　　＜＜<B> * 게임의 설명 *</B>＞＞</font></TD>
</TR><TR>
<TD bgcolor=$TD_C4 height=5>
<TABLE border="0"><TBODY>
<TR>
<TD bgcolor=$TD_C1><img src="$IMG/$kchara.gif"></TD>
<TD bgcolor=$TD_C2>$simg</TD>
<TD bgcolor=$TD_C3>$timg</TD>
<TD bgcolor=$TD_C4 WIDTH=100% align=center>
<TABLE bgcolor=$TABLE_C border="0">
<TBODY>
<TR>
<TD bgcolor=$TD_C2>이름</TD>
<TD bgcolor=$TD_C3>레벨</TD>
<TD bgcolor=$TD_C2>속성</TD>
<TD bgcolor=$TD_C3>직업</TD>
</TR>
<TR>
<TD bgcolor=$TD_C2>$kname</TD>
<TD bgcolor=$TD_C3 align=right>$klv</TD>
<TD bgcolor=$TD_C2>$ELE[$kele]속</TD>
<TD bgcolor=$TD_C3>$SYOKU[$kclass]</TD>
</TR>
<TR>
<TD bgcolor=$TD_C2>소지금</TD>
<TD bgcolor=$TD_C1 colspan=3 align=right>$kgold GOLD</TD>
</TR>
</TBODY></TABLE>
</TD>
</TR>
</TBODY></TABLE>
</TD>
</TR>
<TR>
<TD height="5">
<TABLE  border="0"><TBODY>
<TR><TD bgcolor=$TD_C4><img src="$IMG/wiz.gif" title="삼국지 모의전투 NET 가이드"></TD><TD width="100%" height=100 bgcolor=$TALK_BG><font size=3 color=$TALK_FONT>$P_MES[$in{'num'}]</font></TD>

</TR>
</TBODY></TABLE>
</TD>
</TR>
<TR>
<TD>
EOM
	$new_num = $in{'num'}+1;
if($new_num < @P_MES){
print "<form action=\"$FILE_ENTRY\" method=\"post\">
<input type=hidden name=id value=$kid>
<input type=hidden name=num value=$new_num>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=RESISDENTS>
<input type=submit value=\"다음에\"></form>";
}
print<<"EOM";
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="게임을 시작한다"></form>

</TD>
</TR>
</TBODY></TABLE>
EOM

	&FOOTER;
	exit;
}
1;