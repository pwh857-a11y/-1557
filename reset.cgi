
sub RESET_MODE{

	# MAIN DATA
	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			unlink("$dir/$file");
		}
	}
	closedir(dirlist);

	# COMMAND DATA
	$dir="./charalog/command";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			unlink("$dir/$file");
		}
	}
	closedir(dirlist);

	$dir="./charalog/command1";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			unlink("$dir/$file");
		}
	}
	closedir(dirlist);

	$dir="./charalog/per";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			unlink("$dir/$file");
		}
	}
	closedir(dirlist);

	$dir="./charalog/bak";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			unlink("$dir/$file");
		}
	}
	closedir(dirlist);

	# LOG DATA
	$dir="./charalog/log";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			unlink("$dir/$file");
		}
	}
	closedir(dirlist);

	$dir="./charalog/log2";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			unlink("$dir/$file");
		}
	}
	closedir(dirlist);

	$dir="./charalog/log3";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			unlink("$dir/$file");
		}
	}
	closedir(dirlist);

	$dir="./charalog/history";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			unlink("$dir/$file");
		}
	}
	closedir(dirlist);

	# NEW DATA
	@NEW_DATA = ();

	# ACT LOG
	$actfile = "./log_file/act_log.cgi";
	open(OUT,">$actfile");
	print OUT @NEW_DATA;
	close(OUT);

	# BBS LIST
	open(OUT,">$BBS_LIST");
	print OUT @NEW_DATA;
	close(OUT);

	open(OUT,">$BBS_LIST1");
	print OUT @NEW_DATA;
	close(OUT);

	open(OUT,">$BBS_LIST2");
	print OUT @NEW_DATA;
	close(OUT);

	open(OUT,">./log_file/admin_bbs\.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# COUNTRY LIST
	open(OUT,">$COUNTRY_LIST");
	print OUT @NEW_DATA;
	close(OUT);

	# COUNTRY_LIST2 LIST
	open(OUT,">$COUNTRY_LIST2");
	print OUT @NEW_DATA;
	close(OUT);

	# DATE LIST
	open(OUT,">./log_file/date_count.cgi");
	print OUT @NEW_DATA;
	close(OUT);

	# DEF LIST
	open(OUT,">$DEF_LIST");
	print OUT @NEW_DATA;
	close(OUT);

	# MAP LOG LIST
	open(OUT,">$MAP_LOG_LIST");
	print OUT @NEW_DATA;
	close(OUT);

	# MAP LOG LIST2
	open(OUT,">$MAP_LOG_LIST2");
	print OUT @NEW_DATA;
	close(OUT);

	# MESSAGE LIST
	open(OUT,">$MESSAGE_LIST");
	print OUT @NEW_DATA;
	close(OUT);

	# MESSAGE2 LIST
	open(OUT,">$MESSAGE_LIST2");
	print OUT @NEW_DATA;
	close(OUT);

	# COUNTRY NO
	open(OUT,">$COUNTRY_NO_LIST");
	print OUT @NEW_DATA;
	close(OUT);

	# TRAP NO
	open(OUT,">$TRAP_LIST");
	print OUT @NEW_DATA;
	close(OUT);

	# COUNTRY MES
	open(OUT,">$COUNTRY_MES");
	print OUT @NEW_DATA;
	close(OUT);

	# LOCAL_LIST
	open(OUT,">$LOCAL_LIST");
	print OUT @NEW_DATA;
	close(OUT);

	# UNIT_LIST
	open(OUT,">$UNIT_LIST");
	print OUT @NEW_DATA;
	close(OUT);

	open(IN,"$F_TOWN_LIST");
	@F_T_DATA = <IN>;
	close(IN);

	# TOWN LIST
	open(OUT,">$TOWN_LIST");
	print OUT @F_T_DATA;
	close(OUT);

	# TOWN2 LIST
	open(OUT,">$TOWN_LIST2");
	print OUT @F_T_DATA;
	close(OUT);


	&MAP_LOG("전 데이터를 초기화했습니다.");
}
1;

