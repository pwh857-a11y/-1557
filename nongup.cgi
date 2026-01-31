
sub NONGUP{
						$ksub2=0;
						if($kgold<50){
							&K_LOG("$mmonth월 : 자금부족으로 실행할 수 없었습니다.");
						}elsif($znou >= $znou_max){
							&K_LOG("$mmonth월 : 농업치가 최고입니다.");
							$znou = $znou_max;
						}else{
							if($kskill =~ /Aa/){
							$znouadd = int(int($kintt)/8 + rand($kintt) / 15);
							}else{
							$znouadd = int(int($kintt)/12 + rand($kintt) / 20);
							}


							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /농업/){
										if($qup =~ /농업/){
										$kqpoint += $znouadd;
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

							if($kcodea =~ /B4/ && 5 > rand(100)){
								$kqpoint += 1;
								&K_LOG("$mmonth월 : [$kname]: 「음, 창비호가 말한 보물이 이건가? 가지고 가야지.」");
							}


							if($kcodea =~ /B7/ && 7 > rand(100)){
								$kqpoint += 1;
								&K_LOG("$mmonth월 : [$kname]: 「음, 탐스러운 딸기를 발견했다. 딸기를 1개 땄다.」");
							}

							if($kcodea =~ /A8|D4/){
							$kqpoint += $znouadd;
							}

							$znou += $znouadd;
							$kgold -= 50;
							if($znou > $znou_max){
								$znou = $znou_max;
							}
							$kcex += 30;
							$kexp += 30;
							$kpoint += 10;
							if("$zname" ne ""){
								splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
							}
							&K_LOG("$mmonth월 : $zname의 농업을 <font color=red>+$znouadd</font> 개발했습니다.");
							$kint_ex++;
							$go_ex += int($kbank/5);
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
						}
}
1;

