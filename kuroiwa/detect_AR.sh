for textfile in $( ls -F | grep -v / ); do
	
	if [[ $textfile =~ mes.utf$ ]]; then
		echo "!!!!! ${textfile} !!!!!!"
		ret=`cat ${textfile} | pcregrep -M  '■AR.*(\n|.)*次週の' | sed '$d' | sed  "/---/d" | sed "1d" | sed "/^[<space><tab>]*$/d" | sed "s/●//" | sed "s/◎//" | sed "s/・//" | sed "s/-//" | sed "s/－//" | sed "s/>//" | sed "s/　*//" | sed "s/ *//" `
		cat << EOS
	fi
$ret
EOS
done