for file in BulkGraviton_hh_htatahbb_narrow_M*
do
  mv "$file" "${file/_htatahbb_/_htatahcc_}"
done