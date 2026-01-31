
sub SUBIDAE{
						$ksub2=0;
						if($kgold<50){
							&K_LOG("$mmonth월 : 자금부족으로 실행할 수 없었습니다.");
						}elsif($zshiro >= $zshiro_max){
							$zshiro = $zshiro_max;
							&K_LOG("$mmonth월 : 더이상 수비대 양성을 할 수 없습니다.");
						}else{
							if($kskill =~ /Da/){
							$zshiroadd = int(($kstrt + rand($kstrt))*1.25);
							}else{
							$zshiroadd = $kstrt + int(rand($kstrt));
							}

							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /수비/){
										if($qup =~ /수비/){
										$kqpoint += $zshiroadd;
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

							if($kcodea =~ /A6/){
								$kqpoint += $zshiroadd;
							}

							$zshiro += $zshiroadd;
							$kgold -= 50;
							if($zshiro > $zshiro_max){
								$zshiro = $zshiro_max;
							}
							$kcex += 30;
							$kexp += 30;
							$kpoint += 10;
							if("$zname" ne ""){
								splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
							}
							&K_LOG("$mmonth월 : $zname성의 수비대를 <font color=red>+$zshiroadd</font>명 양성했습니다.");
							$kstr_ex++;
							$go_ex += int($kbank/5);
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
						}
}
1;

