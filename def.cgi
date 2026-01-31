
sub DEF{
						$ksub2=0;
						if($kgold<50){
							&K_LOG("$mmonth월 : 자금부족으로 실행할 수 없었습니다.");
						}elsif($zdef_att >= 1000){
							$zdef_att = 1000;
							&K_LOG("$mmonth월 : 방어시설이 최고치입니다.");
						}else{
							$zdef_att_add = int(($kleat/12) + rand($kleat) / 20);
							$zdef_att += $zdef_att_add;
							$kgold -= 50;
							if($zdef_att > 1000){
								$zdef_att = 1000;
							}


							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /방어/){
										if($qup =~ /방어/){
										$kqpoint += $zdef_att_add;
										}else{
										$kqpoint += $qup;
										}
										if($qtalkd eq ""){
										}else{
										&K_LOG("$mmonth월 : $qtalkd");
										}
									}	
								}
							}
							$kqpoint += $zdef_att_add if $kcodea =~ /A2/;
							if($kcodea =~ /C5/ && 6 > rand(100)){
								$kqpoint += 1;
								&K_LOG("$mmonth월 : [창비호] 사부님이 저를 버리셨다고요? 으아아아아아아아아아앙! 사부님! 으아앙~");
							}
							$kcex += 30;
							$kexp += 30;
							$kpoint += 10;
							if("$zname" ne ""){
								splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
							}
							&K_LOG("$mmonth월 : $zname의 방어시설을 <font color=red>+$zdef_att_add</font> 강화했습니다.");
							$klea_ex++;
							$go_ex += int($kbank/5);
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
						}
}
1;

