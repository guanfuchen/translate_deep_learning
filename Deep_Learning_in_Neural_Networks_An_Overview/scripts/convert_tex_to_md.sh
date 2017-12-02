for  target in $(find . -name "target")
do
	# echo $target
	for tex_file in $(ls $target/*.tex)
	do
		# echo $tex_file
		tex_file_name=$(basename ${tex_file} .tex)
		# echo $tex_file_name
		pandoc -s $tex_file -o $target/$tex_file_name.md
	done
done
