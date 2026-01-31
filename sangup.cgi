
sub SANGUP{
						$ksub2=0;
						if($kgold<50){
							&K_LOG("$mmonth월 : 자금부족으로 실행할 수 없었습니다.");
						}elsif($zsyo >= $zsyo_max){
							&K_LOG("$mmonth월 : 상업치가 최고입니다.");
							$zsyo = $zsyo_max;						
							}else{
							if($kskill =~ /Ba/){
							$zsyoadd = int(int($kintt)/8 + rand($kintt) / 15);
							}else{
							$zsyoadd = int(int($kintt)/12 + rand($kintt) / 20);
							}

							$zsyo += $zsyoadd;
							$kgold -= 50;
							if($zsyo > $zsyo_max){
								$zsyo = $zsyo_max;
							}

							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /상업/){
										if($qup =~ /상업/){
										$kqpoint += $zsyoadd;
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

							if($kcodea =~ /B1/ && 15 > rand(100)){
								$kqpoint += 1;
								&K_LOG("$mmonth월 : [도연길]: 「오, 이 비단을 비향이가 보냈다고? 잘 쓰겠다고 전해주게나.」");
							}

							if($kcodea =~ /B3/ && 6 > rand(100)){
								if($kstrt > rand(100)){
								$kqpoint += 1;
								&K_LOG("$mmonth월 : [좀도둑]: 「윽, 왕가놈이 사람을 고용했군. 잡혀버렸다! 살려줘!」");
								}else{
								&K_LOG("$mmonth월 : [좀도둑]: 「쿠하하 나를 이기려면 백만년은 멀었다구!」");
								}
							}

							if($kcodea =~ /A3|C3/){
							$kqpoint += $zsyoadd;
							}

							$kcex += 30;
							$kexp += 30;
							$kpoint += 10;
							if("$zname" ne ""){
								splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
							}
							&K_LOG("$mmonth월 : $zname의 상업을 <font color=red>+$zsyoadd</font> 발전시켰습니다.");
							$kint_ex++;
							$go_ex += int($kbank/5);
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
						}
}
1;

