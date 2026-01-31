
sub HAYA{
					if($kcon eq "0"){
					&K_LOG("$mmonth월 : 이미 하야되었습니다.");
					}else{

		open(IN,"$DEF_LIST");
		@DEF_LIST3 = <IN>;
		close(IN);

							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /하야/){
										$kqpoint += $qup;
										if($qtalkd eq ""){
										}else{
										&K_LOG("$mmonth월 : $qtalkd");
										}
									}	
								}
							}


		@NEW_DEF_LIST3=();
		foreach(@DEF_LIST3){
		($did,$dname,$dtown_id,$dtown_flg,$dcon,$dchara,$dsol,$dsub1_ex,$dtown_battle,$ddef) = split(/<>/);
		if("$kid" ne "$did"){
			push(@NEW_DEF_LIST3,"$_");
			}
		}
		open(OUT,">$DEF_LIST");
		print OUT @NEW_DEF_LIST3;
		close(OUT);

					&BONG_DEL;
					$kcon = 0;
					&K_LOG("$mmonth월 : 관직을 버리고 재야인사로 하야했습니다.");
					$kcex = 0;
					$ksol = 0;
					}
}
1;

