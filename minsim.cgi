
sub MINSIM{
						$ksub2=0;
						if($krice<100){
							&K_LOG("$mmonth월 : 쌀이 부족해 실행할 수 없었습니다.");
						}elsif($zpri >= 100){
							&K_LOG("$mmonth월 : 민심을 더이상 올릴 수 없습니다.");
							$zpri=100;
						}else{
							if($kskill =~ /Fa/){
							$zpriadd = int(int($kchat)/20 + rand(int($kchat)) / 15);
							}else{
							$zpriadd = int(int($kchat)/20 + rand(int($kchat)) / 20);
							}
							$zpri += $zpriadd;
							$krice -= 100;
							$kcex += 30;
							$kexp += 30;
							$kpoint += 10;
							if($zpri > 100){
								$zpri=100;
							}


							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /민심/){
										if($qup =~ /민심/){
										$kqpoint += $zpriadd;
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

							if($kcodea =~ /C6/ && 30 > rand(100)){
								if($kintt > rand(200)){
								$kqpoint += 1;
								&K_LOG("$mmonth월 : [방화범] 이크~ 들켰다!");
								&K_LOG("$mmonth월 : 불을 지르려고 시도하던 방화범을 잡았다!");
								}else{
								&K_LOG("$mmonth월 : 방화범에 대한 어떠한 단서도 찾을 수가 없었다.");
								}
							}

							if($kcodea =~ /B5/){
							$kqpoint += $zpriadd;
							}

							if("$zname" ne ""){
								splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
							}

							&K_LOG("$mmonth월 : $zname성의 민심이 <font color=red>+$zpriadd</font> 올랐습니다.");
							$kcha_ex++;
							$go_ex += int($kbank/5);
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
						}
}
1;

