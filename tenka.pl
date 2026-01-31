#_/_/_/_/_/_/_/_/_/_/_/#
#_/    전투 화면    _/#
#_/_/_/_/_/_/_/_/_/_/_/#

sub tenka {

	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&COUNTRY_DATA_OPEN("$kcon");
	&CHARA_ITEM_OPEN;
	&TIME_DATA;

	open(IN,"./data/entry_list.cgi") or &error("등록자 리스트가 열리지 않습니다.");
	@ENTRY = <IN>;
	close(IN);
	$ent=0;
	$entcount=@ENTRY;
	@N_ENTRY=();
	foreach(@ENTRY){
		($tid,$tname,$tchara,$tcon,$tcname,$tcele,$tpoint,$tflg) =split(/<>/);
		if($ent>1){push(@N_ENTRY,"$_");}
		$ent++;
	}
	($wid,$wname,$wchara,$wcon,$wcname,$wcele,$wpoint,$wflg) =split(/<>/,$ENTRY[0]);
	($eid,$ename,$echara,$econ,$ecname,$ecele,$epoint,$eflg) =split(/<>/,$ENTRY[1]);

	
	open(IN,"./data/battle_time.cgi") or &error("타임 데이터가 열리지 않습니다.");
	@CTIME = <IN>;
	close(IN);
	($ctime,$ccount,$ctotal,$clast,$cflg) =split(/<>/,$CTIME[0]);
	if($ccount eq""){$ccount=1;}
	else{$ccount=1;}
	$ctime=time();

	open(IN,"./data/winner_list.cgi") or &error("타임 데이터가 열리지 않습니다.");
	@WIN = <IN>;
	close(IN);
	$ceno=@WIN+1;

	if($entcount<=2){
		$cbtype="결승";
		&maplog("<font color=orange>[천하 제일 결승]</font>결승전：$wname VS $ename의 시합을 했습니다!");
	}elsif($entcount<=4){
		$cbtype="준결승";
		&maplog("<font color=orange>[천하 제일 준결]</font>준결승：$wname VS $ename의 시합을 했습니다!");
	}else{
		$cbtype="제$ceno 시합";
		&maplog("<font color=green>[천하 제일]</font>제$ceno 시합：$wname VS $ename의 시합을 했습니다!");
	}
	&gprint;
	$turn=0;$win=0;$lose=0;
	while($turn<=30){
		$turn++;
		if($turn>100){&error("루프");}
		$bmess="";$bmess1="";$bmess2="";

		if($wab[15] && $wabdmg[15]>$eabdmg[15] && int(rand(3-$wabdmg[15])) eq 0){$sensei = 1;}
		elsif($eab[15] && $eabdmg[15]>$wabdmg[15] && int(rand(3-$eabdmg[15])) eq 0){$sensei = 0;}
		elsif(int(rand($wdex)) > int(rand($edex))){$sensei = 1;}
		else{$sensei = 0;}
		
		if($sensei){
			if($whp>0){
				&wat;
				$bmess.="<table border=0 width=100%><td bgcolor=$ELE_C[2]>$bmess1</td></table>";
			}
			if($ehp>0){
				&eat;
				$bmess.="<table border=0 width=100%><td bgcolor=$ELE_C[1]>$bmess2</td></table>";
			}
		}else{
			if($ehp>0){
				&eat;
				$bmess.="<table width=100%><td bgcolor=$ELE_C[1]>$bmess2</td></table>";
			}if($whp>0){
				&wat;
				$bmess.="<table width=100%><td bgcolor=$ELE_C[2]>$bmess1</td></table>";
			}
		}
		if($win){
			$win_name="$wname";
			$win_id="$wid";
			$lose_name="$ename";
			$lose_id="$eid";

			&bprint;
			push(@N_ENTRY,"$wid<>$wname<>$wchara<>$wcon<>$wcname<>$wcele<>$wpoint<>$wflg<>\n");
			push(@WIN,"$wid<>$wchara<>$wname<>$ename<>$wcon<>$cbtype<>$ctime<>\n");
			$blog.= <<"EOF";
			<center>
			<TABLE border="0" width="400" bgcolor="#000000" CLASS=TC>
  			<TBODY><TR>
      			<TD colspan="2" align="center" bgcolor="$FCOLOR"><FONT color="#ffffcc">시합 종료!</FONT></TD>
    			</TR>
    			<TR><TD colspan="2" align="center" bgcolor="$FCOLOR2"><FONT color="#cc0000">$wname</FONT>의 승리!<BR>
      			</TD></TR>
  			</TBODY></TABLE>
			</center>
EOF
			last;
		}if($lose){
			$win_name="$ename";
			$win_id="$eid";
			$lose_name="$wname";
			$lose_id="$wid";

			&bprint;
			push(@N_ENTRY,"$eid<>$ename<>$echara<>$econ<>$ecname<>$ecele<>$epoint<>$eflg<>\n");
			push(@WIN,"$eid<>$echara<>$ename<>$wname<>$wcon<>$cbtype<>$ctime<>\n");
			$blog.= <<"EOF";
			<center>
			<TABLE border="0" width="400" bgcolor="#000000" CLASS=TC>
  			<TBODY><TR>
      			<TD colspan="2" align="center" bgcolor="$FCOLOR"><FONT color="#ffffcc">시합 종료!</FONT></TD>
    			</TR>
    			<TR><TD colspan="2" align="center" bgcolor="$FCOLOR2"><FONT color="#cc0000">$ename</FONT>의 승리!<BR>
      			</TD></TR>
  			</TBODY></TABLE>
			</center>
EOF
			last;
		}
		&bprint;
	}
	if(!$win && !$lose){
		$win_name="$wname";
		$win_id="$wid";
		$lose_name="$ename";
		$lose_id="$eid";

		push(@N_ENTRY,"$wid<>$wname<>$wchara<>$wcon<>$wcname<>$wcele<>$wpoint<>$wflg<>\n");
		push(@WIN,"$wid<>$wchara<>$wname<>$ename<>$wcon<>$cbtype<>$ctime<>\n");
		$bmess.="결착이 붙지 않았다.";
		&bprint;
	}
	if(@N_ENTRY<=1){
		&maplog("<font color=red>[대회 결과]</font>$win_name가 천하 제일 무도회에서 우승했습니다!상금으로 해서 우승자의$win_name에는 500만 Gold,준우승의$lose_name에는 200만 Gold가 주어졌습니다.");
		$enemy_id="$win_id";
		&enemy_open;
		$ebank+=5000000;
		&enemy_input;

		$enemy_id="$lose_id";
		&enemy_open;
		$ebank+=2000000;
		&enemy_input;

		$ccount=0;
		$ctotal++;
		$cflg=0;
	}
	&log_print;

	open(OUT,">./data/winner_list.cgi") or &error('데이터를 쓸 수 없습니다.');
	print OUT @WIN;
	close(OUT);

	open(OUT,">./data/entry_list.cgi") or &error('데이터를 쓸 수 없습니다.');
	print OUT @N_ENTRY;
	close(OUT);

	@N_TIMEDATA=();
	push(@N_TIMEDATA,"$ctime<>$ccount<>$ctotal<>$clast<>$cflg<>\n");
	open(OUT,">./data/battle_time.cgi") or &error('데이터를 쓸 수 없습니다.');
	print OUT @N_TIMEDATA;
	close(OUT);
}

sub wat{
	if(!$wpara2){
		if($wab[1]){
			$hpsai=int($wabdmg[1]/100*$wmaxhp);
			$whp+=$hpsai;
			if($whp>$wmaxhp){$whp=$wmaxhp;}
			$bmess.="[재생]$wname는 HP가<font color=blue>$hpsai</font>회복했다.<BR>";
		}

		$wkai = int($wspeed/100 + rand($wspeed/100)) + 1;
		if($wkai<1){$wkai=1;}
		if($wkai>=8){$wkai=8;}

		$bmess.="<font color=blue>$wname</font>의$wkai회공격!<BR>";
		if($wpara){
			$whpd=int(rand($wmaxhp*$wpara/10));
			$whp-=$whpd;
			if($whp<=1){$whp=1;}
			$bmess.="<font color=red>독에 의해$whpd의 데미지를 받았다.</font><BR>";
		}
	
		for($kou=0;$kou<$wkai;$kou++){
			$rand=int(rand(100)) ;$at=0;$wsv=0;
			if($wmp/($wmaxmp+1)*100<=$wmprate){$magic=1;}
			elsif($whp/($wmaxhp+1)*100<=$whprate){$magic=2;}
			else{$magic=0;}
			##기술 발동
			$mpdown=$wtec_mp[$magic];
			if($wab[6]){$mpdown-=int($wtec_mp[$magic]*$wabdmg[6]/100);}

			if($wab[25]){
				$whitup=1.5;
			}else{
				$whitup=1;
			}

			if($wtec_hit[$magic]*$whitup>$rand && $mpdown<=$wmp){
				$bmess.="<font color=red size=4><b>$wtec_name[$magic] </b></font>";
				if($wab[6]){$bmess.="<font color=blue><b>(소비 $wabdmg[6]%경감)</b></font>";}
				$wmp-=$mpdown;
				if($wtec_sta[$magic] eq 1){
					$whpup=$wtec_str[$magic] + int(rand($wfai/2));
					$whp+=$whpup;
					if($whp>$wmaxhp){$whp=$wmaxhp;}
					$bmess.="HP가<font color=blue>$whpup</font>회복했다.<BR>";
				}elsif($wtec_sta[$magic] eq 2){
					$whp+=int($wmaxhp/10);
					$wmp+=int($wmaxmp/10);
					if($whp>$wmaxhp){$whp=$wmaxhp;}
					if($wmp>$wmaxmp){$wmp=$wmaxmp;}
					$bmess.="<font color=blue>HP와 MP가 회복했다.</font><BR>";
				}elsif($wtec_sta[$magic] eq 3){
					$wat+=int($wfai*($wtec_str[$magic]/100));
					$bmess.="<font color=blue>공격력이 상승했다.</font><BR>";
				}elsif($wtec_sta[$magic] eq 4){
					$wdef+=int($wfai*($wtec_str[$magic]/100));
					$bmess.="<font color=blue>내구력이 상승했다.</font><BR>";
				}elsif($wtec_sta[$magic] eq 5){
					$wmdef+=int($wfai*($wtec_str[$magic]/100));
					$bmess.="<font color=blue>마법 내구력이 상승했다.</font><BR>";
				}elsif($wtec_sta[$magic] eq 6){
					$wdmg=$etec_str[$magic] + int(rand($wint)) -int($emdef);
					$wsv=6;
					$at=1;
				}elsif($wtec_sta[$magic] eq 7){
					$wsmp=int(rand($emaxmp)/5);
					$emp-=$wsmp;
					if($emp<0){$emp=0;}
					$wmp+=$wsmp;
					if($wmp>$wmaxmp){$wmp=$wmaxmp;}
					$bmess.="$ename의 MP를<font color=red>$wsmp</font>빼앗았다.<BR>";
				}elsif($wtec_sta[$magic] eq 8){
					$ehp=int($ehp-$ehp/$wtec_str[$magic]);
					$bmess.="$ename의 체력이 $wtec_str[$magic]분의 1 감소했다.<BR>";
				}else{
					$wdmg=$wtec_str[$magic] + int(rand($wint)) -int($emdef);
					if($wab[5]){
						$wdmg+=int($wdmg*$wabdmg[5]/100);
						$bmess.="<font color=blue><b>(데미지 +$wabdmg[5]%) </b></font>";
					}
					if($eab[7]){
						$wdmg-=int($wdmg*$eabdmg[7]/100);
						$bmess.="<font color=blue><b>(데미지-$eabdmg[7]%) </b></font>";
					}
					$at=1;
					if($wtec_sta[$magic] eq 9){$wsv=1;$at=1;}#즉사
					if($wtec_sta[$magic] eq 10){$wsv=2;$at=1;}#방어 다운
					if($wtec_sta[$magic] eq 11){$wsv=3;$at=1;}#독
					if($wtec_sta[$magic] eq 12){$wsv=4;$at=1;}#명중 다운
					if($wtec_sta[$magic] eq 13){$wsv=5;$at=1;}#마비
					if($wtec_sta[$magic] eq 14){$wsv=7;$at=1;}#둔화
					
				}
				$bmess.="<br>";
			}else{##통상 공격
				$wdmg=int(rand($wat-$edef/2));
				$at=1;
			}
			if($at){
				##회피·위기
				$hitrand=int(rand(2));
				if($eab[12] && 100>int(rand(1200-$efai))){
					$edmg=int(($wdmg+int(rand($estr)))/2);
					if($edmg<1){$edmg=1;}
					$whp-=$edmg;
					if($whp<1){$whp=1;}
					$wdmg=0;
					$hitrand=0;
					$bmess.="<font color=blue size=3>$ename의 카운터!</font><BR>$wname에<font color=red size=3>$edmg</font>의 데미지를 주었다.";
				}elsif($esh>int(rand(1000))){
					$bmess.="<font color=blue size=3>$ename는 재빠르게 몸을 주고 받았다.</font>";
					$wdmg=0;
					$hitrand=0;
				}elsif($esh2>int(rand(1000))){
					$bmess.="<font color=blue size=3>$ename는 가드 밑.</font>";
					$wdmg=0;
					$hitrand=0;
				}elsif($wcl>int(rand(1000))){
					$bmess.="<font color=blue size=4>위기!</font>";
					$wdmg=int($wdmg*1.5);
					if($wab[23]){
						$wdmg=int($wdmg*$wabdmg[23]);
					}
				}
				##데미지
				if($wdmg<=0 && $hitrand eq 0){
					$wdmg=0;
					$bmess.="<font color=red>$ename</font>에 데미지가 주어지지 않았다.<BR>";
				}elsif($wdmg<=0){
					$wdmg=1;
				}
				if($wdmg){
					$bmess.="<font color=red>$ename</font>에<font color=red size=4>$wdmg</font>의 데미지를 주었다.<BR>";
					if(int(rand(4)) eq 2) < 1){
						$epara=$wabdmg[14];
						if(!$epara){$epara=1;}
						$bmess.="<font color=red>$ename는 독에 범해졌다.</font><BR>";
					}
					elsif($wsv eq 4 && $ehit>20){
						$wsh+=40;
						$bmess.="<font color=red>$ename의 명중율이 내렸다.</font><BR>";
					}
					elsif(int(rand(8)) eq 2 && $wsv eq 5 && $ehit>20){
						$epara2=1;
						$bmess.="<font color=red>$ename는 마비되었다.</font><BR>";
					}
					elsif($wsv eq 6 || $wab[28] && int(rand(4)) eq 1){
						$whpup=int($wdmg/2);
						$whp+=$whpup;
						if($whp>$wmaxhp){$whp=$wmaxhp;}
						$bmess.="$wname는 HP를<font color=blue>$whpup</font>흡수했다.<BR>";
					}
					elsif(int(rand(8)) eq 2 && $wsv eq 7){
						$espeed-=50;
						if($espeed<0){$espeed=0;}
						$bmess.="<font color=red>$ename는 움직임이 늦어졌다.</font><BR>";
					}elsif($wab[26] && int(rand(3)) eq 1){
						$addmg = int(rand(200));
						$bmess.="<font color=red size=2>한층 더<b>$addmg</b>의 추가 데미지를 주었다.</font><BR>";
						$wdmg += $addmg;
					}
					elsif($wab[27] && int(rand(3)) eq 1){
						$msmp=int(rand(150));
						$emp-=$msmp;
						if($emp<0){$emp=0;}
						$wmp+=$msmp;
						if($wmp>$wmaxmp){$wmp=$wmaxmp;}
						$bmess.="$ename의 MP를<font color=red>$msmp</font>빼앗았다.<BR>";
					}
					elsif($wab[31] && int(rand(2)) eq 1){
						$abrand = int(rand(2));
						$iab = $esk[$abrand];
						$atype = $eabtype[$iab];
						if($eab[$atype]){
							$eab[$atype] = 0;
							$bmess.="<font color=red>$ename의 어빌리티 :$eabname[$iab]를 봉했다!</font><BR>";
						}
					}
					if(int(rand(30)) eq 7 && $wsv eq 1 || $wab[9] && int(rand(1000)) < $wabdmg[9]){
						$ehp=0;
						$bmess.="<font color=red>$ename는 즉사했다.</font><BR>";
					}
				}
					$ehp-=$wdmg;
			}
			if($ehp<=0 && $eab[11]  && int(rand(100)) < $eabdmg[11]){
				$ehp=int($emaxhp/2);
				$bmess.="<font color=red>$ename는 부활했다!</font><BR>";
			}elsif($ehp<=0){
				$ehp=0;
				$win=1;
				$bmess.="$ename를 넘어뜨렸다.<BR>";
			}
		
			if($kou>10){&error;}
			if($win){last;}
		}
		$bmess.="<BR>";
	}else{$bmess.="<font color=red>$wname는 움직일 수 없다.</font><BR>";}
	$wpara2=0;
}
sub eat{
	if(!$epara2){
		if($eab[1]){
			$hpsai=int($eabdmg[1]/100*$emaxhp);
			$ehp+=$hpsai;
			if($ehp>$emaxhp){$ehp=$emaxhp;}
			$bmess.="[재생]$ename는 HP가<font color=blue>$hpsai</font>회복했다.<BR>";
		}
		$ekai = int($espeed/100 + rand($espeed/100)) + 1;
		if($ekai<1){$ekai=1;}
		if($ekai>=8){$ekai=8;}

		$bmess.="<font color=red>$ename</font>의$ekai회공격!<BR>";
		if($epara){
			$ehpd=int(rand($emaxhp*$epara/10));
			$ehp-=$ehpd;
			if($ehp<=1){$ehp=1;}
			$bmess.="<font color=red>독에 의해$ehpd의 데미지를 받았다.</font><BR>";
		}
		
		for($kou=0;$kou<$ekai;$kou++){
			$rand=int(rand(100)) ;$at=0;$esv=0;
			if($emp/($emaxmp+1)*100<=$emprate){$magic=1;}
			elsif($ehp/($emaxhp+1)*100<=$ehprate){$magic=2;}
			else{$magic=0;}
			##기술 발동
			$mpdown=$etec_mp[$magic];
			if($eab[6]){$mpdown-=int($etec_mp[$magic]*$eabdmg[6]/100);}

			if($eab[25]){
				$ehitup=1.5;
			}else{
				$ehitup=1;
			}

			if($etec_hit[$magic]*$ehitup>$rand && $mpdown<=$emp){
				$bmess.="<font color=red size=4><b>$etec_name[$magic] </b></font>";
				if($eab[6]){$bmess.="<font color=blue><b>(소비 $eabdmg[6]%경감)</b></font>";}
				$emp-=$mpdown;
				if($etec_sta[$magic] eq 1){
					$ehpup=$etec_str[$magic] + int(rand($efai/2));
					$ehp+=$ehpup;
					if($ehp>$emaxhp){$ehp=$emaxhp;}
					$bmess.="HP가<font color=blue>$ehpup</font>회복했다.<BR>";
				}elsif($etec_sta[$magic] eq 2){
					$ehp+=int($emaxhp/10);
					$emp+=int($emaxmp/10);
					if($ehp>$emaxhp){$ehp=$emaxhp;}
					if($emp>$emaxmp){$emp=$emaxmp;}
					$bmess.="<font color=blue>HP와 MP가 회복했다.</font><BR>";
				}elsif($etec_sta[$magic] eq 3){
					$eat+=int($efai*($etec_str[$magic]/100));
					$bmess.="<font color=blue>공격력이 상승했다.</font><BR>";
				}elsif($etec_sta[$magic] eq 4){
					$edef+=int($efai*($etec_str[$magic]/100));
					$bmess.="<font color=blue>내구력이 상승했다.</font><BR>";
				}elsif($etec_sta[$magic] eq 5){
					$emdef+=int($efai*($etec_str[$magic]/100));
					$bmess.="<font color=blue>마법 내구력이 상승했다.</font><BR>";
				}elsif($etec_sta[$magic] eq 6){
					$edmg=$etec_str[$magic] + int(rand($eint)) -int($wmdef);
					$esv=6;
					$at=1;
				}elsif($etec_sta[$magic] eq 7){
					$esmp=int(rand($wmaxmp)/5);
					$wmp-=$esmp;
					if($wmp<0){$wmp=0;}
					$emp+=$esmp;
					if($emp>$emaxmp){$emp=$emaxmp;}
					$bmess.="$wname의 MP를<font color=red>$esmp</font>빼앗았다.<BR>";
				}elsif($etec_sta[$magic] eq 8){
					$whp=int($whp-$whp/$etec_str[$magic]);
					$bmess.="$wname의 체력이 $etec_str[$magic]분의 1 감소했다.<BR>";
				}else{
					$edmg=$etec_str[$magic] + int(rand($eint)) -int($wmdef);
					if($eab[5]){
						$edmg+=int($edmg*$eabdmg[5]/100);
						$bmess.="<font color=blue><b>(데미지 +$eabdmg[5]%) </b></font>";
					}
					if($wab[7]){
						$edmg-=int($edmg*$wabdmg[7]/100);
						$bmess.="<font color=blue><b>(데미지-$wabdmg[7]%) </b></font>";
					}
					$at=1;
					if($etec_sta[$magic] eq 9){$esv=1;}#즉사
					if($etec_sta[$magic] eq 10){$esv=2;}#방어 다운
					if($etec_sta[$magic] eq 11){$esv=3;}#독
					if($etec_sta[$magic] eq 12){$esv=4;}#명중 다운
					if($etec_sta[$magic] eq 13){$esv=5;}#마비
					if($etec_sta[$magic] eq 14){$esv=7;}#둔화
				}
				$bmess.="<br>";
			}else{##통상 공격
				$edmg=int(rand($eat-$wdef/2));
				$at=1;
			}
			if($at){
				##회피, 위기
				$hitrand=int(rand(2));
				if($wab[12] && 100>int(rand(1200-$wfai))){
					$wdmg=int(($edmg+int(rand($wstr)))/2);
					if($wdmg<1){$wdmg=1;}
					$ehp-=$wdmg;
					if($ehp<1){$ehp=1;}
					$edmg=0;
					$hitrand=0;
					$bmess.="<font color=blue size=3>$wname의 카운터!</font><BR>$ename에<font color=red size=3>$wdmg</font>의 데미지를 주었다.";
				}elsif($wsh>int(rand(1000))){
					$bmess.="<font color=blue size=3>$wname는 재빠르게 몸을 주고 받았다.</font>";
					$edmg=0;
					$hitrand=0;
				}elsif($wsh2>int(rand(1000))){
					$bmess.="<font color=blue size=3>$wname는 가드 밑.</font>";
					$edmg=0;
					$hitrand=0;
				}elsif($ecl>int(rand(1000))){
					$bmess.="<font color=blue size=4>위기!</font>";
					$edmg=int($edmg*1.5);
					if($eab[23]){
						$edmg=int($edmg*$eabdmg[23]);
					}
				}
				##데미지
				if($edmg<=0 && $hitrand eq 0){
					$edmg=0;
					$bmess.="<font color=blue>$wname</font>에 데미지가 주어지지 않았다.<BR>";
				}elsif($edmg<=0){
					$edmg=1;
				}
				if($edmg){
					$bmess.="<font color=blue>$wname</font>에<font color=red size=4>$edmg</font>의 데미지를 주었다.<BR>";
					if($esv eq 2){
						$wdef-=int($wdef/50);
						$bmess.="$wname의 방어력이 내렸다.<BR>";
					}
					elsif(int(rand(4)) eq 2 && $esv eq 3 || $eab[14] && int(rand(6)) < 1){
						$wpara=$eabdmg[14];
						if(!$wpara){$wpara=1;}
						$bmess.="<font color=red>$wname는 독에 범해졌다.</font><BR>";
					}
					elsif($esv eq 4 && $whit>20){
						$esh+=40;
						$bmess.="<font color=red>$wname의 명중율이 내렸다.</font><BR>";
					}
					elsif(int(rand(8)) eq 2 && $esv eq 5){
						$wpara2=1;
						$bmess.="<font color=red>$wname는 마비되었다.</font><BR>";
					}
					elsif($esv eq 6 || $eab[28] && int(rand(4)) eq 1){
						$ehpup=int($edmg/2);
						$ehp+=$ehpup;
						if($ehp>$emaxhp){$ehp=$emaxhp;}
						$bmess.="$ename는 HP를<font color=blue>$ehpup</font>흡수했다.<BR>";
					}
					elsif(int(rand(8)) eq 2 && $esv eq 7){
						$wspeed-=50;
						if($wspeed<0){$wspeed=0;}
						$bmess.="<font color=red>$wname는 움직임이 늦어졌다.</font><BR>";
					}
					elsif($eab[26] && int(rand(3)) eq 1){
						$addmg = int(rand(200));
						$bmess.="한층 더<font color=red size=2><b>$addmg</b></font>의 추가 데미지를 주었다.<BR>";
						$edmg += $addmg;
					}
					elsif($eab[27] && int(rand(3)) eq 1){
						$esmp=int(rand(150));
						$wmp-=$esmp;
						if($wmp<0){$wmp=0;}
						$emp+=$esmp;
						if($emp>$emaxmp){$emp=$emaxmp;}
						$bmess.="$wname의 MP를<font color=red>$esmp</font>빼앗았다.<BR>";
					}
					elsif(int(rand(30)) eq 7 && $esv eq 1 || $eab[9] && int(rand(1000)) < $eabdmg[9]){
						$whp=0;
						$bmess.="<font color=red>$wname는 즉사했다.</font><BR>";
					}
					elsif($eab[31] && int(rand(7)) eq 5){
						$abrand = int(rand(2));
						$iab = $wsk[$abrand];
						$atype = $wabtype[$iab];
						if($wab[$atype]){
							$wab[$atype] = 0;
							$bmess.="<font color=red>$wname의 어빌리티 :$wabname[$iab]를 봉했다!</font><BR>";
						}
					}
				}
				$whp-=$edmg;
			}
			if($whp<=0 && $wab[11]  && int(rand(100)) < $wabdmg[11]){
				$whp=int($wmaxhp/2);
				$bmess.="<font color=red>$wname는 부활했다!</font><BR>";
			}elsif($whp<=0){
				$whp=0;
				$lose=1;
				$bmess.="<font color=red>$wname는 힘이 다했다.</font><BR>";
			}
			if($kou>10){&error("몇회 공격해와 군요");}
			if($lose){last;}
		}
		$bmess.="<BR>";
	}else{$bmess.="<font color=red>$ename는 움직일 수 없다.</font><BR>";}
	$epara2=0;
}

sub gprint{
	$blog.= <<"EOF";
<TABLE border="0" width="100%" align=center height="144" CLASS=TOC>
  <TBODY>
    <TR>
      <TD colspan="3" align="center" bgcolor="$ELE_BG[$town_ele]"><FONT color="#ffffcc">천하 제일 무도회</FONT></TD>
    </TR>
    <TR>
      <TD bgcolor="#cccccc" width="30%">
      <TABLE border="0" width="100%" height="100%" bgcolor=$ELE_BG[$wele] align=right>
        <TBODY>
          <TR>
            <TD rowspan="2"><FONT size="-1"><img src="./img/chara/$wchara.gif"></FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">HP</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$whp/$wmaxhp</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">공격력</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$wstr $chi1(+$warmdmg)</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">무기</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$warmname<BR>
            【$warmdmg/$warmwei】</FONT></TD>
          </TR>
          <TR>
            <TD bgcolor=$FCOLOR2><FONT size="-1">MP</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$wmp/$wmaxmp</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">방어력</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$wvit $chi1(+$wprodmg+$waccdmg)</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">방어구</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$wproname<BR>
            【$wprodmg/$wprowei】</FONT></TD>
          </TR>
          <TR>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$wname</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">직업</FONT></TD>
            <TD bgcolor=$FCOLOR2>$JOB[$wclass]</TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">속도</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$wagi</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">악세사리</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$waccname<BR>
            【$waccdmg/$waccwei】</FONT></TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
      <TD bgcolor="#cccccc" width=30%>
      <TABLE border="0" width="100%" height="100%" bgcolor=$ELE_BG[$eele]>
        <TBODY>
          <TR>
            <TD rowspan="2"><FONT size="-1"><img src="./img/chara/$echara.gif"></FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">HP</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$ehp/$emaxhp</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">공격력</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$estr $chi2(+$earmdmg)</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">무기</FONT></TD>
	    <TD bgcolor=$FCOLOR2><FONT size="-1">$earmname<BR>【$earmdmg/$earmwei】</FONT></TD>
          </TR>
          <TR>
            <TD bgcolor=$FCOLOR2><FONT size="-1">MP</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$emp/$emaxmp</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">방어력</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$evit $chi2(+$eprodmg+$eaccdmg)</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">방어구</FONT></TD>
	    <TD bgcolor=$FCOLOR2><FONT size="-1">$eproname<BR>【$eprodmg/$eprowei】</FONT></TD>
         </TR>
          <TR>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$ename</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">직업</FONT></TD>
            <TD bgcolor=$FCOLOR2>$JOB[$eclass]</TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">속도</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$eagi</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">악세사리</FONT></TD>
	    <TD bgcolor=$FCOLOR2><FONT size="-1">$eaccname<BR>【$eaccdmg/$eaccwei】</FONT></TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
    </TR>
    <TR>
      <TD bgcolor=#000000><font color="white" size="-1">「$wcom」</font></TD>
      <TD bgcolor=#000000><font color="white" size="-1">「$ecom」</font></TD>
    </TR>
  </TBODY>
</TABLE>
<BR><BR>
EOF
}
sub bprint{
	$blog.= <<"EOF";
<CENTER>
<TABLE border="0" width="80%" bgcolor="#000000" CLASS=TC>
  <TBODY>
    <TR>
      <TD colspan="8" align="center" bgcolor="$FCOLOR"><B><FONT color="#ffffcc">$turn 턴</FONT></B></TD>
    </TR>
    <TR>
      <TD colspan="8" align="center" bgcolor="000000"><B><img src=./img/etc/arena.jpg></B></TD>
    </TR>
    <TR>
      <TD bgcolor="$ELE_C[2]" align="center"><IMG src="./img/chara/$wchara.gif"></TD>
      <TD colspan="6" bgcolor="$FCOLOR2" align="center"><font size=2>$bmess</font></TD>
      <TD bgcolor="$ELE_C[1]" align="center"><IMG src="./img/chara/$echara.gif"></TD>
    </TR>
    <TR>
      <TD bgcolor="$ELE_BG[2]" colspan=4 width=12.5%>$wname</TD>
      <TD bgcolor="$ELE_BG[1]" colspan=4 width=12.5%>$ename</TD>
    </TR><TR>
      <TD bgcolor="$ELE_C[2]" width=12.5%>HP</TD>
      <TD bgcolor="$ELE_C[2]" width=12.5%>$whp/$wmaxhp</TD>
      <TD bgcolor="$ELE_C[2]" width=12.5%>MP</TD>
      <TD bgcolor="$ELE_C[2]" width=12.5%>$wmp/$wmaxmp</TD>
      <TD bgcolor="$ELE_C[1]" width=12.5%>HP</TD>
      <TD bgcolor="$ELE_C[1]" width=12.5%>$ehp/$emaxhp</TD>
      <TD bgcolor="$ELE_C[1]" width=12.5%>MP</TD>
      <TD bgcolor="$ELE_C[1]" width=12.5%>$emp/$emaxmp</TD>
    </TR>
  </TBODY>
</TABLE>
</CENTER>
<BR><BR><BR><P>
EOF
}
sub c_open{
	open(IN,"./logfile/chara/$wid.cgi") or &error2('캐릭터 데이터 파일을 열지 않았습니다.');
	@W_DATA = <IN>;
	close(IN);
	($wid,$wpass,$wname,$wurl,$wchara,$wsex,$whp,$wmaxhp,$wmp,$wmaxmp,$wele,$wstr,$wvit,$wint,$wfai,$wdex,$wagi,$wmax,$wcom,$wgold,$wbank,$wex,$wtotalex,$wabp,$wjp,$wcex,$wunit,$wcon,$warm,$wpro,$wacc,$wtec,$wsta,$wpos,$wmes,$whost,$wdate,$wdate2,$wclass,$wtotal,$wkati,$wtype,$woya,$wsk,$wflg,$wflg2,$wflg3,$wflg4,$wflg5) = split(/<>/,$W_DATA[0]);
	$wlv = int($wex/100)+1;

	open(IN,"./logfile/chara/$eid.cgi") or &error2('캐릭터 데이터 파일을 열지 않았습니다.');
	@E_DATA = <IN>;
	close(IN);
	($eid,$epass,$ename,$eurl,$echara,$esex,$ehp,$emaxhp,$emp,$emaxmp,$eele,$estr,$evit,$eint,$efai,$edex,$eagi,$emax,$ecom,$egold,$ebank,$eex,$etotalex,$eabp,$ejp,$ecex,$eunit,$econ,$earm,$epro,$eacc,$etec,$esta,$epos,$emes,$ehost,$edate,$esyo,$eclass,$etotal,$ekati,$etype,$eoya,$esk,$eflg,$eflg2,$eflg3,$eflg4,$eflg5) = split(/<>/,$E_DATA[0]);
	$elv = int($eex/100)+1;
}
sub para{
	#어빌리티 정보
	($wsk[0],$wsk[1]) = split(/,/,$wsk);
	($esk[0],$esk[1]) = split(/,/,$esk);
	open(IN,"./data/ability.cgi");
	@ABILITY = <IN>;
	close(IN);

	foreach(@ABILITY){
		($abno,$abname,$abcom,$abdmg,$abrate,$abpoint,$abclass,$abtype) =split(/<>/);
		if($wsk[0] eq $abno || $wsk[1] eq $abno || $warmsta eq $abno || $wprosta eq $abno || $waccsta eq $abno){
			$wab[$abtype]=1;
			$wabdmg[$abtype]=$abdmg;
			$wabname[$abno]=$abname;
			$wabtype[$abno]=$abtype;
		}
		if($esk[0] eq $abno || $esk[1] eq $abno || $earmsta eq $abno || $eprosta eq $abno || $eaccsta eq $abno){
			$eab[$abtype]=1;
			$eabdmg[$abtype]=$abdmg;
			$eabname[$abno]=$abname;
			$eabtype[$abno]=$abtype;
		}
	}
	#지형 효과
	if($wab[19]){$tup=$wabdmg[19]/100;}
	if($eab[19]){$etup=$eabdmg[19]/100;}
	if($town_ele eq $wele){$waddstr=int($wstr*(0.1 + $tup)) ;$wadddef=int($wvit*(0.1 + $tup)) ;$chi1="<font color=red>↑</font>";}
	if($town_ele eq $eele){$eaddstr=int($estr*(0.1 + $etup)) ;$eadddef=int($evit*(0.1 + $etup)) ;$chi2="<font color=red>↑</font>";}

	#마법검
	if($wab[18]){$warmdmg+=int($wint*$wabdmg[18]/100);}
	if($eab[18]){$earmdmg+=int($eint*$eabdmg[18]/100);}

	#물리 공격 계산
	$wat=$wstr + $warmdmg + int($warmwei/5) + $waddstr;
	if($wab[2]){$wat+=int($wabdmg[2]/100*$wat);}#력 업
	$eat=$estr + $earmdmg + int($earmwei/5) + $eaddstr;
	if($eab[2]){$eat+=int($eabdmg[2]/100*$eat);}#력 업
	
	if($wab[3]){$eat-=int($wabdmg[2]/100*$eat);}#데미지 경감
	if($eab[3]){$wat-=int($eabdmg[2]/100*$wat);}#데미지 경감
	
	#물리 방어 계산
	$wdef=$wvit + $wprodmg + $waccdmg + $wadddef;
	$edef=$evit + $eprodmg + $eaccdmg + $eadddef;

	#마법 방어 계산
	$wmdef=int($wfai/2);
	if(int($wsk/10) eq 4){$wmdef+=int($wsklv) /10*$wmdef;}
	
	$emdef=int($efai/2);

	#위기 계산
	#$wcl=$warmcl;
	$wcl=30;
	$wcl+=int($wdex/4);
	$ecl=30;
	$ecl+=int($edex/4);
	if($wab[10]){$wcl+=$wabdmg[10]*10;}
	if($eab[10]){$ecl+=$eabdmg[10]*10;}
	if($wcl>200){$wcl=200;}
	if($ecl>200){$ecl=200;}

	#회피율 계산
	$wsh=int($wdex/3);
	$esh=int($edex/3);
	if($wab[8]){$wsh2+=$wabdmg[8]*10;}
	if($eab[8]){$esh2+=$eabdmg[8]*10;}

	#공격 회수
	$wadagi=0;
	$eadagi=0;

	if($wab[4]){$wadkai=$wabdmg[4]* 50;}#헤이 파업
	if($eab[4]){$eadkai=$eabdmg[4]* 50;}#헤이 파업
		
	$wspeed=$wagi-$warmwei-$wprowei-$waccwei+$wadagi + $wadkai;
	$espeed=$eagi-$earmwei-$eprowei-$eaccwei+$eadagi + $eadkai;
	
	#HP계산 1
	$whp=$wmaxhp;
	$wmp=$wmaxmp;

	#HP계산 2
	$ehp=$emaxhp;
	$emp=$emaxmp;
}
sub t_open{
	open(IN,"./data/tec.cgi") or &error('파일을 열지 않았습니다.');
	@TEC = <IN>;
	close(IN);
	($wtec1,$wtec2,$wtec3,$wmprate,$whprate) =split(/,/,$wtec);
	
	if($wtec1 eq ""){$wtec1=0;}
	if($wtec2 eq ""){$wtec2=0;}
	if($wtec3 eq ""){$wtec3=0;}

	($wtec_name[0],$wtec_str[0],$wtec_hit[0],$wtec_mp[0],$wtec_ab[0],$wtec_sta[0],$wtec_class[0]) = split(/<>/,$TEC[$wtec1]);
	($wtec_name[1],$wtec_str[1],$wtec_hit[1],$wtec_mp[1],$wtec_ab[1],$wtec_sta[1],$wtec_class[1]) = split(/<>/,$TEC[$wtec2]);
	($wtec_name[2],$wtec_str[2],$wtec_hit[2],$wtec_mp[2],$wtec_ab[2],$wtec_sta[2],$wtec_class[2]) = split(/<>/,$TEC[$wtec3]);
	
	
	($etec1,$etec2,$etec3,$emprate,$ehprate) =split(/,/,$etec);
	if($etec1 eq ""){$etec1=0;}
	if($etec2 eq ""){$etec2=0;}
	if($etec3 eq ""){$etec3=0;}

	($etec_name[0],$etec_str[0],$etec_hit[0],$etec_mp[0],$etec_ab[0],$etec_sta[0],$etec_class[0]) = split(/<>/,$TEC[$etec1]);
	($etec_name[1],$etec_str[1],$etec_hit[1],$etec_mp[1],$etec_ab[1],$etec_sta[1],$etec_class[1]) = split(/<>/,$TEC[$etec2]);
	($etec_name[2],$etec_str[2],$etec_hit[2],$etec_mp[2],$etec_ab[2],$etec_sta[2],$etec_class[2]) = split(/<>/,$TEC[$etec3]);
}
sub eq_open{
	($warmno,$warmname,$warmval,$warmdmg,$warmwei,$warmele,$warmhit,$warmcl,$warmsta,$warmtype,$warmflg) = split(/,/,$warm);
	($wprono,$wproname,$wproval,$wprodmg,$wprowei,$wproele,$wprohit,$wprocl,$wprosta,$wprotype,$wproflg) = split(/,/,$wpro);
	($waccno,$waccname,$waccval,$waccdmg,$waccwei,$waccele,$wacchit,$wacccl,$waccsta,$wacctype,$waccflg) = split(/,/,$wacc);
	if($wele eq "$warmele" && $warmele ne "0"){$warmdmg=int($warmdmg*1.2);}
	if($wele eq "$wproele" && $warmele ne "0"){$wprodmg=int($wprodmg*1.2);}
	if($wele eq "$waccele" && $warmele ne "0"){$waccdmg=int($waccdmg*1.5);}
	if($ARM[$wclass] eq "$warmtype"){$warmhit+=10;}
	
	if($eid){
		($earmno,$earmname,$earmval,$earmdmg,$earmwei,$earmele,$earmhit,$earmcl,$earmsta,$earmtype,$earmflg) = split(/,/,$earm);
		($eprono,$eproname,$eproval,$eprodmg,$eprowei,$eproele,$eprohit,$eprocl,$eprosta,$eprotype,$eproflg) = split(/,/,$epro);
		($eaccno,$eaccname,$eaccval,$eaccdmg,$eaccwei,$eaccele,$eacchit,$eacccl,$eaccsta,$eacctype,$eaccflg) = split(/,/,$eacc);
		if($eele eq "$earmele" && $earmele ne "0"){$earmdmg=int($earmdmg*1.2);}
		if($eele eq "$eproele" && $eproele ne "0"){$eprodmg=int($eprodmg*1.2);}
		if($eele eq "$eaccele" && $eaccele ne "0"){$eaccdmg=int($eaccdmg*1.5);}
		if($ARM[$eclass] eq "$earmtype"){$earmhit+=10;}
	}
}
sub log_print{
	$header = <<"EOM";
	<html>
	<head>
	<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=euc-kr">
	<STYLE type="text/css">
	<!--
A:HOVER{
 color: $ALINK
}
.BC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width :medium; border-color : $ELE_BG[0] $ELE_BG[0] $ELE_BG[0] $ELE_BG[0];border-style : double double double double;background-color : $ELE_BG[0];color : black;}
.TC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width :medium; border-color : $FCOLOR $FCOLOR $FCOLOR $FCOLOR;border-style : double double double double;background-color : $FCOLOR;color : black;}
.CC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width :medium; border-color : $ELE_BG[$con_ele] $ELE_BG[$con_ele] $ELE_BG[$con_ele] $ELE_BG[$con_ele];border-style : double double double double;background-color : $ELE_BG[$con_ele];color : black;}
.CC2 {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width :medium; border-color : $ELE_BG[$con2_ele] $ELE_BG[$con2_ele] $ELE_BG[$con2_ele] $ELE_BG[$con2_ele];border-style : double double double double;background-color : $ELE_BG[$con2_ele];color : black;}
.MC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width :medium; border-color : $ELE_BG[$wele] $ELE_BG[$wele] $ELE_BG[$wele] $ELE_BG[$wele];border-style : double double double double;background-color : $ELE_BG[$wele];color : black;}
.MFC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width : $ELE_BG[$con_ele];border-top-color : $ELE_BG[$con_ele];border-right-color : $ELE_BG[$con_ele];border-bottom-color : $ELE_BG[$con_ele];border-left-color : $ELE_BG[$con_ele];border-style : double double double double;background-color : $ELE_C[$con_ele];color : black;}
.FC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width : $FCOLOR;border-top-color : $FCOLOR;border-right-color : $FCOLOR;border-bottom-color : $FCOLOR;border-left-color : $FCOLOR;border-style : double double double double;background-color : $FCOLOR2;color : black;}
.TOC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width :medium; border-color : $ELE_BG[$town_ele] $ELE_BG[$town_ele] $ELE_BG[$town_ele] $ELE_BG[$town_ele];border-style : double double double double;background-color : $ELE_BG[$town_ele];color : black;}
.dmg { color: #FF0000; font-size: 10pt }
.clit { color: #0000FF; font-size: 10pt }
-->
	</STYLE>
	<title>$TITLE</title></head>
	<body background=\"$BGIF\" bgcolor=\"$BG\">
EOM

	open(OUT,">./data/battle/$ceno.html");
	print OUT $header;
	print OUT $blog;
	print OUT "</BODY></HTML>";
	close(OUT);
}
1;
