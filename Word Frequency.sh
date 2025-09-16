cat words.txt \
  | tr -s ' ' '\n' \
  | sort \
  | uniq -c \
  | sort -k1nr -k2 \
  | awk '{ print $2, $1 }'
