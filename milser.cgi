
sub MILSER{
						$ksub2=0;
						if($kgold < 100){
							&K_LOG("$mmonth월 : 금이 충분하지 않습니다.");
						}elsif($xmark < $BATTLE_STOP && $con_num >= $CON_ENTRY_MAX){
						&E_ERR("그 나라는 정원을 넘기고 있으므로 입국할 수가 없습니다.");
						}else{
							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /밀서/){
										$kqpoint += $qup;
										if($qtalkd eq ""){
										}else{
										&K_LOG("$mmonth월 : $qtalkd");
										}
									}	
								}
							}


							$kgold-= int(200 - $cha);
							$kcex += 30;
							$kexp += 30;
							$kpoint += 10;
							open(IN,"$MESSAGE_LIST2");
							@MES_REG2 = <IN>;
							close(IN);
							$mes_num = @MES_REG2;
							if($mes_num > $MES_MAX) { pop(@MES_REG2); }
							unshift(@MES_REG2,"$cnum<>$kid<>$kpos<>$kname<>$csub<>$cno<>$ctime<>$kchara<>$cend<>\n");
							open(OUT,">$MESSAGE_LIST2");
							print OUT @MES_REG2;
							close(OUT);
							&K_LOG("$mmonth월 : $cno에게 밀서를 보냈습니다.");
							&MAP_LOG("<img src=$IMG/j21.gif> $cno님이 누군가와 밀담을 나누고 있습니다.");
							$kcha_ex++;
							$go_ex += int($kbank/5);
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
						}
}
1;

