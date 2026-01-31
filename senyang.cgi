
sub senyang{
			if(open(IN,"./charalog/main/$cnum\.cgi")){
			@E_DATA = <IN>;
			close(IN);
			($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$E_DATA[0]);
			if($econ eq $kcon){
			open(IN,"$COUNTRY_LIST") or &ERR2('파일을 열지 않았습니다. err no :country');
			@COU_DATA = <IN>;
			close(IN);
			for($i=0;$i<@COU_DATA;$i++){
			($xvcid,$xvname,$xvele,$xvmark,$xvking,$xvmes,$xvsub,$xvpri) = split(/<>/,$COU_DATA[$i]);
			if($xvcid eq $kcon){
			splice(@COU_DATA,$i,1,"$xvcid<>$xvname<>$xvele<>$xvmark<>$eid<>$xvmes<>$xvsub<>$xvpri<>\n");
			last;
								}
							}
							&MAP_LOG2("<font color=red>[계승]</font>$xvname국의 차기군주로 $ename님이 선정되었습니다.");
							&MAP_LOG("<font color=red>[계승]</font>$xvname국의 차기군주로 $ename님이 선정되었습니다.");
							&K_LOG("$ename에게 왕권을 선양하였습니다.");
							$cou_king[$kcon] = $eid;
							$kclass = int($kclass*3/4);
						}else{
							&K_LOG("$ename님은 아국의 장수가 아닙니다.");
						}

					}else{
						&K_LOG("선양가능한 상대가 없습니다.");
					}	
}
1;

