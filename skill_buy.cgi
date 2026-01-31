sub SKILL_BUY {

	if($in{'no'} eq ""){&ERR("NO:가 입력되지 않습니다.");}
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&TIME_DATA;
	open(IN,"$SKILL_LIST");
	@SKILL_DATA = <IN>;
	close(IN);
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
<table align="center" cellpadding="0" cellspacing="0" width="945">
    <tr>
        <td width="945">
            <p><img src="$IMG/up.gif" width="950" height="93" border="0"></p>
        </td>
    </tr>
    <tr>
        <td width="945" height="545" background="$IMG/backg.gif">
            <table align="center" cellpadding="0" cellspacing="0" width="749" bordercolordark="white" bordercolorlight="black">
                <tr>
                    <td width="749" height="11" colspan="14">
                    </td>
                </tr>
                <tr>
                    <td width="749" height="60" colspan="14" bgcolor="black">
                        <p><span style="font-size:9pt;"><b>특기교육소</b><br>특기포인트를 이용하여 
                        이 곳에서 특기를 배울 수 있습니다.<br>현재 $kname님께서는 
                        <font color="red"><b>$kpoint 특기포인트</b></font>를 가지고 계십니다<br>해당 특기 이미지에 
                        마우스를 갖다대면 특기에 대한 자세한 설명을 볼 수 있습니다.</span></p>
                    </td>
                </tr>
                <tr>
                    <td width="749" height="8" colspan="14">
                    </td>
                </tr>
                <tr>
                    <td width="92" height="97">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p align="center"><img src="$IMG/skill1a.jpg" width="80" height="80" border="0" alt="농업치를 소폭 상승시킨다.
포인트:1000"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="0">
<input type=hidden name=mode value=56>
<input type=submit value="  배운다  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="10" height="522" rowspan="5">
                    </td>
                    <td width="92" height="97">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill2a.jpg" width="80" height="80" border="0" alt="상업치를 소폭 상승시킨다.
포인트:1000"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="3">
<input type=hidden name=mode value=56>
<input type=submit value="  배운다  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="10" height="522" rowspan="5">
                    </td>
                    <td width="92" height="97">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill3a.jpg" width="80" height="80" border="0" alt="기술치를 소폭 상승시킨다.
포인트:1000"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="6">
<input type=hidden name=mode value=56>
<input type=submit value="  배운다  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="10" height="522" rowspan="5">
                    </td>
                    <td width="92" height="97">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill4a.jpg" width="80" height="80" border="0" alt="수비대양성을 소폭 상승시킨다.
포인트:1000"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="9">
<input type=hidden name=mode value=56>
<input type=submit value="  배운다  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="10" height="522" rowspan="5">
                    </td>
                    <td width="92" height="154">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill5a.jpg" width="80" height="80" border="0" alt="병력의 훈련이나 맹훈련시 훈련도를 상승시킨다.
포인트:1000"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="12">
<input type=hidden name=mode value=56>
<input type=submit value="  배운다  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="10" height="522" rowspan="5">
                    </td>
                    <td width="92" height="154">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill6at.jpg" width="80" height="80" border="0" alt="민심을 상승시킨다.
포인트:1000"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="15">
<input type=hidden name=mode value=56>
<input type=submit value="  배운다  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="10" height="522" rowspan="5">
                        <p>&nbsp;</p>
                    </td>
                    <td width="91" height="154">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill7a.jpg" width="80" height="80" border="0" alt="병력의 훈련상한도를 120으로 올린다.
포인트:1000"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="18">
<input type=hidden name=mode value=56>
<input type=submit value="  배운다  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="46" height="522" rowspan="5">
                        <p>&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td width="92" height="30">
                        <p align="center">↓</p>
                    </td>
                    <td width="92" height="30">
                        <p align="center">↓</p>
                    </td>
                    <td width="92" height="30">
                        <p align="center">↓</p>
                    </td>
                    <td width="92" height="30">
                        <p align="center">↓</p>
                    </td>
                    <td width="92" height="30">
                        <p align="center">↓</p>
                    </td>
                    <td width="92" height="30">
                        <p align="center">↓</p>
                    </td>
                    <td width="91" height="30">
                        <p align="center">↓</p>
                    </td>
                </tr>
                <tr>
                    <td width="92" height="103">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill1bt.jpg" width="80" height="80" border="0" alt="[특기농업필수]
거래상한을 5000으로 상승시키고 송금 상한이 10000으로 늘어난다.
포인트:1850"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value=1>
<input type=hidden name=mode value=56>
<input type=submit value="  배운다  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="92" height="103">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill2b.jpg" width="80" height="80" border="0" alt="[특기상업필수]
물품거래시 더 비싸게 판다.
포인트:2000"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="4">
<input type=hidden name=mode value=56>
<input type=submit value="  배운다  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="92" height="103">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill3b.jpg" width="80" height="80" border="0" alt="[특기기술필수]
함정을 100% 확률로 피한다.
포인트:2000"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="7">
<input type=hidden name=mode value=56>
<input type=submit value="  배운다  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="92" height="103">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill4b.jpg" width="80" height="80" border="0" alt="[특기양성필수]
징병을 해도 농민이 줄지 않는다.
징병에 필요한 최소농민은 있어야 하고 성의 민심이 75이상이어야 한다.
포인트:2000"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="10">
<input type=hidden name=mode value=56>
<input type=submit value="  배운다  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="92" height="154">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill5b.jpg" width="80" height="80" border="0" alt="[특기훈련필수]
하위병종 보병,궁병,창병,중장보병의 공격력,수비력을 +20한다.
포인트:2000"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="13">
<input type=hidden name=mode value=56>
<input type=submit value="  배운다  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="92" height="154">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill6b.jpg" width="80" height="80" border="0" alt="[특기민심필수]
황건적의 수비력에 매력을 가산한다.
포인트:1800"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="16">
<input type=hidden name=mode value=56>
<input type=submit value="  배운다  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="91" height="154">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill7b.jpg" width="80" height="80" border="0" alt="[특기고양필수]
자신의 전술포인트가 20% 상승한다.
포인트:1950"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="19">
<input type=hidden name=mode value=56>
<input type=submit value="  배운다  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td width="92" height="30">
                        <p align="center">↓</p>
                    </td>
                    <td width="92" height="30">
                        <p align="center">↓</p>
                    </td>
                    <td width="92" height="30">
                        <p align="center">↓</p>
                    </td>
                    <td width="92" height="30">
                        <p align="center">↓</p>
                    </td>
                    <td width="92" height="30">
                        <p align="center">↓</p>
                    </td>
                    <td width="92" height="30">
                        <p align="center">↓</p>
                    </td>
                    <td width="92" height="30">
                        <p align="center">↓</p>
                    </td>
                </tr>
                <tr>
                    <td width="92" height="107">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill1c.jpg" width="80" height="80" border="0" alt="[특기거래필수]
어느 지역에서든 기술치에 상관하지 않고 원하는 병종을 징병가능하다.
포인트:3200"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="2">
<input type=hidden name=mode value=56>
<input type=submit value="  배운다  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="92" height="107">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill2c.jpg" width="80" height="80" border="0" alt="[특기수완필수]
병종 '황실근위병'의 가격을 50% 다운시킨다.
포인트:2500"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="5">
<input type=hidden name=mode value=56>
<input type=submit value="  배운다  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="92" height="107">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill3c.jpg" width="80" height="80" border="0" alt="[특기회피필수]
발석거의 성공격력에 지력이 가산된다.
포인트:2300"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="8">
<input type=hidden name=mode value=56>
<input type=submit value="  배운다  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="92" height="107">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill4c.jpg" width="80" height="80" border="0" alt="[특기모병필수]
함정설치시 위력이 2배로 상승하고 함정설치시 공헌치 2배가 된다.
포인트:2500"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="11">
<input type=hidden name=mode value=56>
<input type=submit value="  배운다  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="92" height="154">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill5c.jpg" width="80" height="80" border="0" alt="[특기독려필수]
자국의 성이 아닌 타국의 성에서도 출병이 가능하다.
포인트:3500"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="14">
<input type=hidden name=mode value=56>
<input type=submit value="  배운다  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="92" height="154">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill6c.jpg" width="80" height="80" border="0" alt="[특기매료필수]
매력을 무력에 가산한다.
단, 모든 병종의 가격이 2배가 된다.
포인트:3200"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="17">
<input type=hidden name=mode value=56>
<input type=submit value="  배운다  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                    <td width="91" height="154">
                        <table border="1">
                            <tr>
                                <td width="70">
                                    <p><img src="$IMG/skill7c.jpg" width="80" height="80" border="0" alt="[특기병략필수]
공격시 일기토가 발동되면 50%의 확률로
단 1합에 적에게 승리하여 자신의 무력만큼의 피로도를 추가하고 피해를 준 수치만큼 추가 SP를 받는다.
포인트:3300"></p>
                                </td>
                            </tr>
                            <tr>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
                                <td width="70">
$no_list
<input type=hidden name=select value="20">
<input type=hidden name=mode value=56>
<input type=submit value="  배운다  ">
                                </td>
				</form>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td width="749" height="34" colspan="14">

                    </td>
                </tr>
                <tr>
		<form action="$FILE_STATUS" method="post">
                    <td width="749" height="45" colspan="14" bgcolor="black">
                            <p align="center"><input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="메뉴로 돌아온다">
                    </td>
		    </form>
                </tr>
                <tr>
                    <td width="749" height="18" colspan="14">
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
1;