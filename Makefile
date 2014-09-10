all: pyencodetools/base.py

clean:
	rm classes_template.py pyencodetools/base.py

classes_template.py: 
	python parse_schemas.py

pyencodetools/base.py: classes_template.py
	cat base_template.py $< > $@
