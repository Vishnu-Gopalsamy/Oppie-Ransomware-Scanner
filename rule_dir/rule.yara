import "pe"
rule my_rule {
	meta:
		KEY = "VALUE"
	strings:
		$name = "hello"
	condition:
		any of them
}
