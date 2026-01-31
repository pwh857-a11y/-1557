
sub ILGITO{



							open(IN,"./charalog/main/$cnum\.cgi");
							@E_DATA = <IN>;
							close(IN);
							($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$E_DATA[0]);
							($estr_ex,$eint_ex,$elea_ex,$echa_ex,$esub1_ex,$esub2_ex,$ebo_ex,$egi_ex,$ech_ex,$egu_ex,$ego_ex,$ejin_ex) = split(/,/,$esub1);

							if($kpos != $epos){
							&K_LOG("$mmonth월 : 상대방과 같은 위치에 있지 않습니다.");
							}else{
							
										&CHARA_ITEM_OPEN;

										$kche = 100;
										$eche = 100;

										if($csub == 1){
										&K_LOG4("\[$old_date\]$ename(무력:$estrt 통솔:$eleat)님과 일기토를 시작!");
										&E_LOG4("\[$old_date\]$kname(무력:$kstrt 통솔:$kleat)님과 일기토를 시작!");



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

										if($kcodea =~ /B8/){
											if(119 < $estr+$elea){
											$kqpoint += 1;
											&K_LOG("$mmonth월 : [$kname]: 「음, $ename을 상대로 일기토에서 승리했군. 기분좋은걸?」");
											}else{
											&K_LOG("$mmonth월 : [$kname]: 「윽, 낭패다. 능력치가 너무 낮은 상대를 골랐어.」");
											}
										}

							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /일기토/){
										$kqpoint += $qup;
										if($qtalkd eq ""){
										}else{
										&K_LOG("$mmonth월 : $qtalkd");
										}
									}	
								}
							}


										&MAP_LOG("<img src=$IMG/j25.gif> $kname님이 $ename님을 상대로 일기토에서 승리!");
										&K_LOG4("\[$old_date\]$kname님이 $ename님을 상대로 일기토에서 승리!");
										&E_LOG4("\[$old_date\]$kname님이 $ename님을 상대로 일기토에서 승리!");
										}else{
										&MAP_LOG("<img src=$IMG/j25.gif> $ename님이 $kname님을 상대로 일기토에서 승리!");
										&K_LOG4("\[$old_date\]$ename님이 $kname님을 상대로 일기토에서 승리!");
										&E_LOG4("\[$old_date\]$ename님이 $kname님을 상대로 일기토에서 승리!");
										}

										}elsif($csub == 2){
										&K_LOG4("\[$old_date\]$ename(지력:$eintt 매력:$echat)님과 설전을 시작!");
										&E_LOG4("\[$old_date\]$kname(지력:$kintt 매력:$kchat)님과 설전을 시작!");
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
											$wine = 1;
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
										&K_LOG4("<font color=red>$count</font>회:$kname의 정신력($kstrt) $kche (-$edmge\) VS $ename의 정신력($estrt) $eche (-$kdmge\)");
										}

										if($wine){
										if($kcodea =~ /B8/){
											if(149 < $eint+$echa){
											$kqpoint += 1;
											&K_LOG("$mmonth월 : [$kname]: 「음, $ename을 상대로 설전에서 승리했군. 기분좋은걸?」");
											}else{
											&K_LOG("$mmonth월 : [$kname]: 「윽, 낭패다. 능력치가 너무 낮은 상대를 골랐어.」");
											}
										}

							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /설전/){
										$kqpoint += $qup;
										if($qtalkd eq ""){
										}else{
										&K_LOG("$mmonth월 : $qtalkd");
										}
									}	
								}
							}


										&MAP_LOG("<img src=$IMG/j26.gif> $kname님이 $ename님을 상대로 설전에서 승리!");
										&K_LOG4("\[$old_date\]$kname님이 $ename님을 상대로 설전에서 승리!");
										&E_LOG4("\[$old_date\]$kname님이 $ename님을 상대로 설전에서 승리!");
										}elsif(!$wine){
										&MAP_LOG("<img src=$IMG/j26.gif> $ename님이 $kname님을 상대로 설전에서 승리!");
										&K_LOG4("\[$old_date\]$ename님이 $kname님을 상대로 설전에서 승리!");
										&E_LOG4("\[$old_date\]$ename님이 $kname님을 상대로 설전에서 승리!");
										}


							}
						}	
}
1;

