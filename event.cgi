#!C:\xampp\perl\bin\perl.exe

use lib 'C:\xampp\htdocs';
require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

if($MENTE) { &ERR2("스크립트 체크를 위해 일시적으로 정지합니다."); }
&DECODE;
&COUNTRY_DATA_OPEN("$kcon");
&CHARA_MAIN_OPEN;

if($mode eq 'TOP') { &TOP; }
elsif($mode eq 'TOP_NEW'){&TOP_NEW;}
else{&TOP0;}



sub TOP_NEW {
	&CHARA_MAIN_OPEN;
	&CHARA_ITEM_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&COUNTRY_DATA_OPEN("$kcon");

	if($jin_ex){
		&ERR('이미 참가한 상태입니다.');
	}

	open(IN,"./log_file/event_on.cgi");
	@EVENT = <IN>;
	close(IN);

	($eventon,$emoney,$etime) = split(/<>/,$EVENT[0]);

	$emoney += 100;

	@EVENT_DATA=();
	unshift(@EVENT_DATA,"$eventon<>$emoney<>$etime<>");
	open(OUT,">./log_file/event_on.cgi") or &ERR('MAIN 새로운 데이터를 기입할 수 없습니다.');
	print OUT @EVENT_DATA;
	close(OUT);

	$kgold -= 100;
	$jin_ex += 1;

	$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
	&CHARA_MAIN_INPUT;
	&HEADER;
print <<"EOM";
<CENTER><hr size=0><h2>금 100을 지불하고 무쌍대회에 참가하였습니다. [총누적금액 : $emoney]</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="확인"></form></CENTER>
EOM

	&FOOTER;

	exit;

}




sub TOP0 {
	&CHARA_MAIN_OPEN;
	&CHARA_ITEM_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&COUNTRY_DATA_OPEN("$kcon");



	if($jin_ex eq ""){
		&ERR('신청하지 않은 상태이거나 현재 이미 탈락한 상태입니다.');
	}

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR("파일 오픈 에러!");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);

	@tmp = map {(split /<>/)[10]} @CL_DATA;
	@CL_DATA = @CL_DATA[sort {rand} 0 .. $#tmp];
	foreach(@no){
		$no_list .= "<input type=hidden name=no value=$_>"
	}


	$thing = 0;
	foreach(@CL_DATA) {
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/);
		($estr_ex,$eint_ex,$elea_ex,$echa_ex,$esub1_ex,$esub2_ex,$ebo_ex,$egi_ex,$ech_ex,$egu_ex,$ego_ex,$ejin_ex) = split(/,/,$esub1);			
		if($ejin_ex == 1){ 
		$thing++;
		}
	}


	if($thing == 1){
	open(IN,"./log_file/event_on.cgi");
	@EVENT = <IN>;
	close(IN);

	($eventon,$emoney) = split(/<>/,$EVENT[0]);
		$kgold += $emoney;
		&CHARA_MAIN_INPUT;

		$emoney = 0;
		$eventon = 3;
	@EVENT_DATA=();
	unshift(@EVENT_DATA,"$eventon<>$emoney<>");
	open(OUT,">./log_file/event_on.cgi") or &ERR('MAIN 새로운 데이터를 기입할 수 없습니다.');
	print OUT @EVENT_DATA;
	close(OUT);
		&MAP_LOG("<img src=$IMG/j27.gif> 천하무쌍대회에서 $kname님이 우승을 거머쥐었습니다!");


	@NEW_DATA = ();

	$timefile = "./log_file/event_time.cgi";
	open(OUT,">$timefile");
	print OUT @NEW_DATA;
	close(OUT);

		&ERR('[축 <b>우승</b> 축]<br>축하합니다.<br>최후의 1인까지 남았습니다.<br>상금 $emoney 를 획득하셨습니다!');


	}


	&HEADER;
	$no = $in{'no'} + 1;

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
            <table cellpadding="0" cellspacing="0" width="752" height="488" bordercolordark="white" bordercolorlight="black" background="$IMG/cola.jpg">
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
                                    <p><font color="white"><span style="font-size:9pt;">$cou_name[$kcon]</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$kstrt</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$kintt</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$kleat</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$kchat</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$kgold</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$krice</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$kcex</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$ksol</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$kgat</span></font></p>
                                </td>
                            </tr>
                        </table>

                    </td>
                    <td width="25" height="236" rowspan="4">
                    </td>
                    <td width="70" height="34">
                    </td>
                    <td width="24" height="236" rowspan="4">
                  </td>
                    <td width="421" height="467" rowspan="6">
<TABLE border=0 width=100% height=80%><TR><TD>
<center><form action=event.cgi method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<p>[일기토&설전 상대를 선택]<BR><select name=num>
<option value="">장수를 선택
EOM


	foreach(@CL_DATA) {
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/);
		($estr_ex,$eint_ex,$elea_ex,$echa_ex,$esub1_ex,$esub2_ex,$ebo_ex,$egi_ex,$ech_ex,$egu_ex,$ego_ex,$ejin_ex) = split(/,/,$esub1);			
		if($eid eq $kid) { next; }
		if($ejin_ex == 1){
		if($econ eq "" || $econ eq 0){
		$con_l2 .= "<option value=$eid>????? 《재야》\n";
		}else{
		$con_l2 .= "<option value=$eid>????? 《$cou_name[$econ]》\n";
		}
		}
	}

print <<"EOM";
$con_l
$con_l2
</select>
$no_list
<BR><br>[겨루기 방식]<br>
<select name=ilgiselect size="1">
<option value="1">일기토로 승부 (무력,통솔 영향)
<option value="2">설전으로 승부 (지력,매력 영향)
</select>
<center><br><input type=hidden name=mode value=TOP>
<input type=submit value="천하무쌍대회시작"></form>


<center><form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="돌아온다"></center></center></form></CENTER>
</TD></TR></TABLE>
                    </td>
                    <td width="8" height="467" rowspan="6">
                    </td>
                </tr>
                <tr>
                    <td width="70" height="82">
                        <p align="center"><img src="$IMG/$kchara.gif" width="64" height="80" border="0"></p>
                    </td>
                </tr>
                <tr>
                    <td width="70" height="37">
                        <p align="center"><font color="white" face="돋움"><span style="font-size:9pt;">$kname</span></font></p>
                    </td>
                </tr>
                <tr>
                    <td width="70" height="83">
                    </td>
                </tr>
                <tr>
                    <td width="312" height="35" colspan="5">
                    </td>
                </tr>
                <tr>
                    <td width="288" height="196" colspan="4" valign="up">
<font color="white" face="돋움"><span style="font-size:9pt;">누구인지 모르는 미지의 상대와 자신있는 겨루기방식으로 대결합니다.<br>누가 누군지 모르기 때문에 겨루기방식을 잘 선택하셔야 합니다.<br>지는 쪽은 무조건 탈락이고 최후의 1인이 남을때까지 계속해서 싸웁니다.</span></font></td>
                    <td width="24" height="196">
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






sub TOP{

	&EVENT_TIME_LIST;




							open(IN,"./charalog/main/$in{'num'}\.cgi");
							@E_DATA = <IN>;
							close(IN);
							($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$E_DATA[0]);
							($estr_ex,$eint_ex,$elea_ex,$echa_ex,$esub1_ex,$esub2_ex,$ebo_ex,$egi_ex,$ech_ex,$egu_ex,$ego_ex,$ejin_ex) = split(/,/,$esub1);

							
										&CHARA_ITEM_OPEN;

										$kche = 100;
										$eche = 100;

										if($in{'ilgiselect'} == 1){
										&K_LOG4("\[무쌍대회\]$ename(무력:$estrt 통솔:$eleat)님과 일기토를 시작!");
										&E_LOG4("\[무쌍대회\]$kname(무력:$kstrt 통솔:$kleat)님과 일기토를 시작!");



										for($count=1;$count<60;$count++){

										if($kche <= 0){last;}

										$kdmge = int((($kstrt+$kleat)/50)+rand(($kstrt+$kleat)/10));
										$edmge = int((($estrt+$eleat)/50)+rand(($estrt+$eleat)/10));

										if($kdmge < 1){
											$kdmge=1;	
										}

							

										$eche -= $kdmge;

										if($eche <= 0){
											&K_LOG4("<font color=red>$count</font>합:$kname의 체력 $kche (-$edmge\) VS $ename의 체력 $eche (-$kdmge\)");
											&E_LOG4("<font color=red>$count</font>합:$kname의 체력 $kche (-$edmge\) VS $ename의 체력 $eche (-$kdmge\)");
											$wine = 1;
										last;
										}
										
										if($edmge < 1){
											$edmge=1;	
										}

										$kche -= $edmge;

										if($kche <= 0){
											&K_LOG4("<font color=red>$count</font>합:$kname의 체력 $kche (-$edmge\) VS $ename의 체력 $eche (-$kdmge\)");
											&E_LOG4("<font color=red>$count</font>합:$kname의 체력 $kche (-$edmge\) VS $ename의 체력 $eche (-$kdmge\)");
											last;
										}
										&K_LOG4("<font color=red>$count</font>합:$kname의 체력 $kche (-$edmge\) VS $ename의 체력 $eche (-$kdmge\)");
										}




										if($wine){

										&K_LOG4("\[무쌍대회]$kname님이 $ename님을 상대로 일기토에서 승리!");
										&E_LOG4("\[무쌍대회]$kname님이 $ename님을 상대로 일기토에서 승리!");
										$ejin_ex = "";
										$esub1 = "$estr_ex,$eint_ex,$elea_ex,$echa_ex,$esub1_ex,$esub2_ex,$ebo_ex,$egi_ex,$ech_ex,$egu_ex,$ego_ex,$ejin_ex,";
										&ENEMY_INPUT;
										}else{
										&K_LOG4("\[무쌍대회]$ename님이 $kname님을 상대로 일기토에서 승리!");
										&E_LOG4("\[무쌍대회]$ename님이 $kname님을 상대로 일기토에서 승리!");
										$jin_ex = "";
										$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
										&CHARA_MAIN_INPUT;
										}

										}elsif($in{'ilgiselect'} == 2){

										&K_LOG4("\[무쌍대회]$ename(지력:$eintt 매력:$echat)님과 설전을 시작!");
										&E_LOG4("\[무쌍대회]$kname(지력:$kintt 매력:$kchat)님과 설전을 시작!");
										for($count=1;$count<60;$count++){

										if($kche <= 0){last;}

										$kdmge = int((($kintt+$kchat)/50)+rand(($kintt+$kchat)/10));
										$edmge = int((($eintt+$echat)/50)+rand(($eintt+$echat)/10));

										if($kdmge < 1){
											$kdmge=1;	
										}

							

										$eche -= $kdmge;

										if($eche <= 0){
											$eche = 0;
											&K_LOG4("<font color=red>$count</font>회:$kname의 정신력 $kche (-$edmge\) VS $ename의 정신력 $eche (-$kdmge\)");
											&E_LOG4("<font color=red>$count</font>회:$kname의 정신력 $kche (-$edmge\) VS $ename의 정신력 $eche (-$kdmge\)");
											$wine1 = 1;
										last;
										}
										
										if($edmge < 1){
											$edmge=1;	
										}

										$kche -= $edmge;

										if($kche <= 0){
											$kche = 0;
											&K_LOG4("<font color=red>$count</font>회:$kname의 정신력 $kche (-$edmge\) VS $ename의 정신력 $eche (-$kdmge\)");
											&E_LOG4("<font color=red>$count</font>회:$kname의 정신력 $kche (-$edmge\) VS $ename의 정신력 $eche (-$kdmge\)");
											last;
										}
										&K_LOG4("<font color=red>$count</font>회:$kname의 정신력 $kche (-$edmge\) VS $ename의 정신력 $eche (-$kdmge\)");
										}
										if($wine1){
										&K_LOG4("\[무쌍대회]$kname님이 $ename님을 상대로 설전에서 승리!");
										&E_LOG4("\[무쌍대회]$kname님이 $ename님을 상대로 설전에서 승리!");
										$ejin_ex = "";
										$esub1 = "$estr_ex,$eint_ex,$elea_ex,$echa_ex,$esub1_ex,$esub2_ex,$ebo_ex,$egi_ex,$ech_ex,$egu_ex,$ego_ex,$ejin_ex,";
										&ENEMY_INPUT;
										}else{
										&K_LOG4("\[무쌍대회]$ename님이 $kname님을 상대로 설전에서 승리!");
										&E_LOG4("\[무쌍대회]$ename님이 $kname님을 상대로 설전에서 승리!");
										$jin_ex = "";
										$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
										&CHARA_MAIN_INPUT;
										}
										}







	open(IN,"./charalog/log3/$kid.cgi");
	@LOG_DATA2 = <IN>;
	close(IN);
	$p=0;
	while($p<20){$log_list2 .= "<font color=navy>●</font>$LOG_DATA2[$p]<BR>";$p++;}							


	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>$ename님과 승부를 겨뤘습니다.</h2><p>
$log_list2
<form action="./event.cgi" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=submit value="확인"></form></CENTER>
EOM

	&FOOTER;

	exit;

							}