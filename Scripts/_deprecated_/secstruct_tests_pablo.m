
rdatdir = 'ALLRDAT/';
outputdir = 'rnastructure_results/';

% FN glycine riboswitch

name = 'FNGly';
rdatname = 'FN.Lig.COMBINED.COHCOA.SQR.rdat';
sequen = 'GGCAAUUCGAGUAGAAUUGACAGAGAGGAUAUGAGGAGAGAUUUCAUUUUAAUGAAACACCGAAGAAGUAAAUCUUUCAGGUAAAAAGGACUCAUAUUGGACGAACCUCUGGAGAGCUUAUCUAAGAGAUAACACCGAAGGAGCAAAGCUAAUUUUAGCCUAAACUCUCAGGUAAAAGGACGGAGAAAACACAAGUUCAGGAGUACUGAACCAAAGAAACAACAACAACAAC';
struct = '..((((((.....))))))........((((((((......((((((....)))))).(((...((((.....))))..)))........))))))))........(((((......(((((.....))))).(((...((((....((((....)))).....))))..))).......))))).........((((((.....)))))).....................';


run_test_suite(name, [rdatdir, rdatname], struct, outputdir);
close all
% P4P6

name = 'P4P6';
rdatname = 'P4P6.COMBINED.COHCOA.SQR.rdat';
sequen = 'GGCCAAAACAACGGAAUUGCGGGAAAGGGGUCAACAGCCGUUCAGUACCAAGUCUCAGGGGAAACUUUGAGAUGGCCUUGCAAAGGGUAUGGUAAUAAGCUGACGGACAUGGUCCUAACCACGCAGCCAAGUCCUAAGUCAACAGAUCUUCUGUUGAUAUGGAUGCAGUUCAAAACCAAACCAAAGAAACAACAACAACAAC';
struct = '.................((((((...((((((.....(((.((((.(((..(((((((((....)))))))))..((.......))....)))......)))))))....))))))..)).))))((...((((...(((((((((...)))))))))..))))...)).................................';


run_test_suite(name, [rdatdir, rdatname], struct, outputdir);
close all

% 5S rRNA

name = '5SrRNA';
rdatname = '5S.COMBINED.COHCOA.SQR.rdat';
sequen = 'GGAAAGCAAUUCGAGUAGAAUUGGAAAGGGAAAGAAAUGCCUGGCGGCCGUAGCGCGGUGGUCCCACCUGACCCCAUGCCGAACUCAGAAGUGAAACGCCGUAGCGCCGAUGGUAGUGUGGGGUCUCCCCAUGCGAGAGUAGGGAACUGCCAGGCAUAAAACAGUUAAGGAGUACUUAACAAACAAAGAAACAACAACAACAAC';
struct = '......((((((.....))))))...............(((((((((.....((((((((....(((((((.............))))..)))...)))))).)).((.......((((((((...)))))))).......))...)))))))))........((((((.....))))))........................';


run_test_suite(name, [rdatdir, rdatname], struct, outputdir);
close all
% tRNA

name = 'tRNA';
rdatname = 'tRNA.COMBINED.COHCOA.SQR.rdat';
sequen = 'GGAACAAACAAAACAGCGGAUUUAGCUCAGUUGGGAGAGCGCCAGACUGAAGAUCUGGAGGUCCUGUGUUCGAUCCACAGAAUUCGCACCAAAACGUUAAGGAGUACUUAACCAAAGAAACAACAACAACAAC';
struct = '...............(((((((..((((........)))).((((.........)))).....(((((.......))))))))))))........((((((.....)))))).....................';


run_test_suite(name, [rdatdir, rdatname], struct, outputdir);
close all
% cdiGMP riboswitch

name = 'cdiGMP';
rdatname = 'cdiGMP.COMBINED.COHCOA.SQR.rdat';
sequen = 'GGAAAAAUGUCACGCACAGGGCAAACCAUUCGAAAGAGUGGGACGCAAAGCCUCCGGCCUAAACCAGAAGACAUGGUAGGUAGCGGGGUUACCGAUGGCAAAAUGCAUACAAACCGUUAAGGAGUACUUAACAAAGAAACAACAACAACAAC';
struct = '..........((((......((...((((((....))))))...))...(((.((((((((..((.........)))))))..))))))...)).))..................((((((.....))))))....................';


run_test_suite(name, [rdatdir, rdatname], struct, outputdir);
close all
% ADD riboswitch

name = 'add';
rdatname = 'ADD.COMBINED.COHCOA.SQR.rdat';
sequen = 'GGAAAGCAAUUCGAGUAGAAUUGGAAAGGGAAAGAAACGCUUCAUAUAAUCCUAAUGAUAUGGUUUGGGAGUUUCUACCAAGAGCCUUAAACUCUUGAUUAUGAAGUGAAAACAAAGUUAAGGAGUACUUAACACAAAGAAACAACAACAACAAC';
struct = '......((((((.....))))))..............(((((((((...((((((.........))))))........((((((.......))))))..)))))))))........((((((.....))))))......................';


run_test_suite(name, [rdatdir, rdatname], struct, outputdir);
close all

% Class1 ligase (with SHAPEKnots)

name = 'c1l';
rdatname = 'C1L.COMBINED.COHCOA.SQR.rdat';
sequen = 'GGAACCGCGAGUAGCGGAAAUCCAGUAGGAACACUAUACUACUGGAUAAUCAAAGACAAAUCUGCCCGAAGGGCUUGAGAACAUCGAAACACGAUGCAGAGGUGGCAGCCUCCGGUGGGUUAAAACCCAACGUUCUCAACAAUAGUGAAAAGCGCGAGUAGCGCAACAAAGAAACAACAACAACAAC';
struct = '....((((.....))))...[[[[[[[[...((((((.]]]]]]]]...............[[[[[(...).(.((((((((((.........)))..((((.]]]]]))))((((((((....)))))))))))))))).))))))....((((.....)))).......................';


run_test_suite(name, [rdatdir, rdatname], struct, outputdir);

% AdoCob (with SHAPEKnots)

name = 'adocbl';
rdatname = 'AdoCbl.Lig.COMBINED.COHCOA.SQR.rdat';
sequen = 'GGAACAGCCCGAGUAGGGCCGGCAGGUGCUCCCGACCCUGCGGUCGGGAGUUAAAAGGGAAGCCGGUGCAAGUCCGGCACGGUCCCGCCACUGUGACGGGGAGUCGCCCCUCGGGAUGUGCCACUGGCCCGAAGGCCGGGAAGGCGGAGGGGCGGCGAGGAUCCGGAGUCAGGAAACCUGCCUGCCGGCGCGAGUAGCGCAAACGAAAGAAACAACAACAACAAC';
struct = '......((((.....))))((((((((((((((((((....))))))))))....(((...(((((.......)))))[[(((...))).(((...((((..((((((((((......((((.((((((....))))))...)))))))))))))).....))))..]])))....)))))))))))((((.....)))).........................';

run_test_suite(name, [rdatdir, rdatname], struct, outputdir);

% GIR1 (with SHAPEKnots)

name = 'gir1';
rdatname = 'GIR1.COMBINED.COHCOA.SQR.rdat';
sequen = 'GGUUGGGUUGGGAAGUAUCAUGGCUAAUCACCAUGAUGCAAUCGGGUUGAACACUUAAUUGGGUUAAAACGGUGGGGGACGAUCCCGUAACAUCCGUCCUAACGGCGACAGACUGCACGGCCCUGCCUCUUAGGUGUGUUCAAUGAACAGUCGUUCCGAAAGGAAGCAUCCGGUAUCCCAAGACAAUC';
struct = '(((((..(((((..(((((((((.......)))))))))..((((.((((((((......(((((...((((((((((....))))....)).))))((....)).....[[[[[...))))).((((...))))))))))))....]]]]].((((....))))....))))...)))))..)))))';

run_test_suite(name, [rdatdir, rdatname], struct, outputdir);
