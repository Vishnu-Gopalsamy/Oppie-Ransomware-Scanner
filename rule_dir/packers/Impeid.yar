rule Stelth_PE_101_BGCorp: PEiD
{
    strings:
        $a = { ?? ?? ?? ?? ?? BA ?? ?? ?? 00 }
        $b = { BA ?? ?? ?? 00 }
    condition:
        for any of ($*) : ( $ at pe.entry_point )

}
rule Stelth_PE_101_BGCorp_additional: PEiD
{
    strings:
        $a = { BA ?? ?? ?? 00 }
    condition:
        $a at pe.entry_point

}