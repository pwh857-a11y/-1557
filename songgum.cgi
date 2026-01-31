
sub SONGGUM{
					if($kgold<0){
					&K_LOG("돈이 충분하지 않습니다.");
					}else{
					$susu = int($csub/10);
					$susu1 = $csub-$susu;
					&K_LOG("$cno님에게 $susu1의 금을 송금했습니다. [수수료: $susu]");
					$kgold-=$csub;

							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /송금/){
										if($qup =~ /송금/){
										$kqpoint += $susu1;
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

					$kcex += int($csub/250);
					$kexp += int($csub/250);
					$kpoint += int($csub/500);
					$go_ex += int($kbank/5);
					$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
					open(IN,"./charalog/main/$cnum\.cgi");
					@E_DATA = <IN>;
					close(IN);
					($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$E_DATA[0]);
					$egold += $susu1;
					&E_LOG2("$kname님에게서 $susu1의 금을 송금받았습니다. [수수료: $susu]");
					&ENEMY_INPUT;
							
					}
}
1;

