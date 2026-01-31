
sub EDONG{
						$ksub2=0;
						$zhit=0;
						foreach(@z){
							if($_ eq $cnum){
								$zhit=1;
							}
						}

						if($zhit){
							($zzname,$zzcon,$zznum,$zznou,$zzsyo,$zzshiro,$zznou_max,$zzsyo_max,$zzshiro_max,$zzpri,$zzx,$zzy,$zzsouba,$zzdef_att,$zzsub1,$zzsub2,$zz[0],$zz[1],$zz[2],$zz[3],$zz[4],$zz[5],$zz[6],$zz[7],$zzname1,$zzname2,$zzbong1,$zzbong2,$zzbong3) = split(/<>/,$TOWN_DATA[$cnum]);
							if($zzcon eq $kcon){


		open(IN,"$DEF_LIST");
		@DEF_LIST3 = <IN>;
		close(IN);

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


							$kpos = $cnum;
							$klea_ex++;
							$go_ex += int($kbank/5);
							if($xcid ne "0"){
								$kcex += 20;
								$kexp += 20;
								$kpoint += 8;
							}
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
							&K_LOG("$mmonth월 : $town_name[$cnum]에 이동했습니다.");



							}else{
							if($ksol < 500 || $kskill =~ /Ec/){

		open(IN,"$DEF_LIST");
		@DEF_LIST3 = <IN>;
		close(IN);

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


							$kpos = $cnum;
							$klea_ex++;
							$go_ex += int($kbank/5);
							if($xcid ne "0"){
								$kcex += 20;
								$kexp += 20;
								$kpoint += 8;
							}
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
							&K_LOG("$mmonth월 : $town_name[$cnum]에 이동했습니다.");

							}elsif($ksol >= 500){
							&K_LOG("$mmonth월 : 병력이 500이상 많아 이동할 수 없습니다.");
							}
						}

						}else{
							&K_LOG("$mmonth월 : $town_name[$cnum]에 이동할 수 없습니다. [현재위치 : $zname]");
						}
}
1;
