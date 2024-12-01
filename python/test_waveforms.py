import pytest
import numpy as np

"""
Tests for waveforms.

To run all tests, type pytest at top level like:
    pytest

To run only the tests in this file, do this:
    pytest -q python/test_waveforms.py
"""


class TestPhasor:

    def test_phasor_60Hz(self, phasor_list):
        res = phasor_list[0].get_block_of_samples()
        assert res == [0.0, 0.0007317073170731706, 0.0014634146341463412, 0.002195121951219512, 0.0029268292682926825, 0.0036585365853658534, 0.004390243902439024, 0.0051219512195121945, 0.005853658536585365, 0.006585365853658536, 0.007317073170731707, 0.008048780487804878, 0.008780487804878048, 0.00951219512195122, 0.010243902439024389, 0.01097560975609756, 0.01170731707317073, 0.012439024390243901, 0.013170731707317073, 0.013902439024390242, 0.014634146341463414, 0.015365853658536585, 0.016097560975609757, 0.016829268292682924, 0.017560975609756096, 0.018292682926829267, 0.01902439024390244, 0.01975609756097561, 0.020487804878048778, 0.02121951219512195, 0.02195121951219512, 0.02268292682926829, 0.02341463414634146, 0.02414634146341463, 0.024878048780487803, 0.025609756097560974, 0.026341463414634145, 0.027073170731707313, 0.027804878048780485, 0.028536585365853656, 0.029268292682926828, 0.03, 0.03073170731707317, 0.03146341463414634, 0.03219512195121951, 0.032926829268292684, 0.03365853658536585, 0.03439024390243902, 0.03512195121951219, 0.03585365853658536, 0.036585365853658534, 0.037317073170731706, 0.03804878048780488, 0.03878048780487805, 0.03951219512195122, 0.04024390243902439, 0.040975609756097556, 0.04170731707317072, 0.04243902439024389, 0.043170731707317056, 0.04390243902439022, 0.044634146341463385, 0.045365853658536556, 0.04609756097560972, 0.046829268292682885, 0.04756097560975606, 0.04829268292682922, 0.049024390243902385, 0.04975609756097555, 0.05048780487804872, 0.051219512195121886, 0.05195121951219505, 0.052682926829268215, 0.053414634146341386, 0.05414634146341455, 0.054878048780487715, 0.055609756097560886, 0.05634146341463405, 0.057073170731707215, 0.05780487804878038, 0.05853658536585355, 0.059268292682926715, 0.05999999999999988, 0.06073170731707305, 0.061463414634146216, 0.06219512195121938, 0.06292682926829254, 0.06365853658536572, 0.06439024390243887, 0.06512195121951204, 0.06585365853658522, 0.06658536585365837, 0.06731707317073155, 0.06804878048780472, 0.06878048780487787, 0.06951219512195105, 0.07024390243902422, 0.07097560975609737, 0.07170731707317055, 0.07243902439024372, 0.07317073170731687, 0.07390243902439005, 0.0746341463414632, 0.07536585365853637, 0.07609756097560955, 0.0768292682926827, 0.07756097560975588, 0.07829268292682905, 0.0790243902439022, 0.07975609756097538, 0.08048780487804855, 0.08121951219512172, 0.0819512195121949, 0.08268292682926807, 0.08341463414634125, 0.08414634146341443, 0.0848780487804876, 0.08560975609756077, 0.08634146341463395, 0.08707317073170713, 0.0878048780487803, 0.08853658536585347, 0.08926829268292664, 0.08999999999999983, 0.090731707317073, 0.09146341463414617, 0.09219512195121936, 0.09292682926829253, 0.0936585365853657, 0.09439024390243887, 0.09512195121951206, 0.09585365853658523, 0.0965853658536584, 0.09731707317073159, 0.09804878048780476, 0.09878048780487793, 0.0995121951219511, 0.10024390243902428, 0.10097560975609746, 0.10170731707317063, 0.1024390243902438, 0.10317073170731698, 0.10390243902439016, 0.10463414634146333, 0.10536585365853651, 0.10609756097560968, 0.10682926829268286, 0.10756097560975603, 0.10829268292682921, 0.10902439024390238, 0.10975609756097555, 0.11048780487804873, 0.11121951219512191, 0.11195121951219508, 0.11268292682926825, 0.11341463414634144, 0.11414634146341461, 0.11487804878048778, 0.11560975609756095, 0.11634146341463414, 0.11707317073170731, 0.11780487804878048, 0.11853658536585367, 0.11926829268292684, 0.12000000000000001, 0.12073170731707318, 0.12146341463414637, 0.12219512195121954, 0.12292682926829271, 0.12365853658536588, 0.12439024390243907, 0.12512195121951225, 0.12585365853658542, 0.1265853658536586, 0.12731707317073176, 0.12804878048780494, 0.1287804878048781, 0.12951219512195128, 0.13024390243902445, 0.13097560975609765, 0.13170731707317082, 0.132439024390244, 0.13317073170731716, 0.13390243902439034, 0.1346341463414635, 0.13536585365853668, 0.13609756097560988, 0.13682926829268305, 0.13756097560975622, 0.1382926829268294, 0.13902439024390256, 0.13975609756097573, 0.1404878048780489, 0.1412195121951221, 0.14195121951219528, 0.14268292682926845, 0.14341463414634162, 0.1441463414634148, 0.14487804878048796, 0.14560975609756113, 0.14634146341463433, 0.1470731707317075, 0.14780487804878067, 0.14853658536585385, 0.14926829268292702, 0.1500000000000002, 0.15073170731707336, 0.15146341463414653, 0.15219512195121973, 0.1529268292682929, 0.15365853658536607, 0.15439024390243924, 0.15512195121951242, 0.1558536585365856, 0.15658536585365876, 0.15731707317073196, 0.15804878048780513, 0.1587804878048783, 0.15951219512195144, 0.16024390243902462, 0.16097560975609781, 0.161707317073171, 0.16243902439024416, 0.16317073170731733, 0.1639024390243905]

    def test_phasor_600Hz(self, phasor_list):
        res = phasor_list[1].get_block_of_samples()
        assert res == [0.0, 0.007317073170731707, 0.014634146341463414, 0.02195121951219512, 0.029268292682926828, 0.036585365853658534, 0.04390243902439024, 0.05121951219512195, 0.058536585365853655, 0.06585365853658537, 0.07317073170731707, 0.08048780487804878, 0.08780487804878048, 0.09512195121951218, 0.10243902439024388, 0.10975609756097557, 0.11707317073170727, 0.12439024390243897, 0.13170731707317068, 0.13902439024390237, 0.14634146341463408, 0.15365853658536577, 0.16097560975609748, 0.1682926829268292, 0.1756097560975609, 0.18292682926829265, 0.19024390243902436, 0.19756097560975608, 0.2048780487804878, 0.2121951219512195, 0.21951219512195122, 0.22682926829268293, 0.23414634146341465, 0.24146341463414636, 0.24878048780487808, 0.2560975609756098, 0.26341463414634153, 0.27073170731707324, 0.27804878048780496, 0.2853658536585367, 0.2926829268292684, 0.3000000000000001, 0.3073170731707318, 0.3146341463414635, 0.32195121951219524, 0.32926829268292696, 0.3365853658536586, 0.3439024390243903, 0.351219512195122, 0.35853658536585364, 0.36585365853658536, 0.373170731707317, 0.38048780487804873, 0.3878048780487804, 0.39512195121951205, 0.40243902439024376, 0.4097560975609754, 0.41707317073170713, 0.4243902439024388, 0.4317073170731705, 0.43902439024390216, 0.4463414634146338, 0.45365853658536553, 0.4609756097560972, 0.4682926829268289, 0.47560975609756057, 0.4829268292682922, 0.49024390243902394, 0.4975609756097556, 0.5048780487804873, 0.512195121951219, 0.5195121951219507, 0.5268292682926823, 0.534146341463414, 0.5414634146341457, 0.5487804878048774, 0.556097560975609, 0.5634146341463407, 0.5707317073170725, 0.5780487804878041, 0.5853658536585358, 0.5926829268292675, 0.5999999999999992, 0.6073170731707308, 0.6146341463414625, 0.6219512195121942, 0.6292682926829258, 0.6365853658536575, 0.6439024390243893, 0.651219512195121, 0.6585365853658528, 0.6658536585365845, 0.6731707317073162, 0.680487804878048, 0.6878048780487798, 0.6951219512195115, 0.7024390243902433, 0.709756097560975, 0.7170731707317067, 0.7243902439024386, 0.7317073170731703, 0.739024390243902, 0.7463414634146338, 0.7536585365853655, 0.7609756097560972, 0.7682926829268291, 0.7756097560975608, 0.7829268292682925, 0.7902439024390243, 0.797560975609756, 0.8048780487804877, 0.8121951219512196, 0.8195121951219513, 0.826829268292683, 0.8341463414634148, 0.8414634146341465, 0.8487804878048782, 0.8560975609756101, 0.8634146341463418, 0.8707317073170736, 0.8780487804878053, 0.885365853658537, 0.8926829268292689, 0.9000000000000006, 0.9073170731707323, 0.9146341463414641, 0.9219512195121958, 0.9292682926829275, 0.9365853658536594, 0.9439024390243911, 0.9512195121951228, 0.9585365853658546, 0.9658536585365863, 0.973170731707318, 0.9804878048780499, 0.9878048780487816, 0.9951219512195133, 0.0024390243902450955, 0.009756097560976802, 0.01707317073170851, 0.024390243902440215, 0.031707317073171926, 0.03902439024390363, 0.04634146341463533, 0.05365853658536704, 0.06097560975609875, 0.06829268292683045, 0.07560975609756217, 0.08292682926829388, 0.09024390243902557, 0.09756097560975727, 0.10487804878048897, 0.11219512195122067, 0.11951219512195237, 0.12682926829268407, 0.13414634146341578, 0.14146341463414747, 0.14878048780487918, 0.15609756097561087, 0.16341463414634258, 0.1707317073170743, 0.178048780487806, 0.18536585365853772, 0.19268292682926946, 0.20000000000000118, 0.2073170731707329, 0.2146341463414646, 0.22195121951219632, 0.22926829268292803, 0.23658536585365975, 0.24390243902439146, 0.2512195121951232, 0.2585365853658549, 0.2658536585365866, 0.2731707317073183, 0.28048780487805003, 0.28780487804878174, 0.2951219512195135, 0.3024390243902452, 0.30975609756097694, 0.31707317073170865, 0.32439024390244037, 0.331707317073172, 0.33902439024390374, 0.3463414634146354, 0.35365853658536706, 0.36097560975609877, 0.36829268292683043, 0.37560975609756214, 0.3829268292682938, 0.39024390243902546, 0.3975609756097572, 0.40487804878048883, 0.41219512195122054, 0.4195121951219522, 0.4268292682926839, 0.4341463414634156, 0.44146341463414723, 0.44878048780487895, 0.4560975609756106, 0.4634146341463423, 0.470731707317074, 0.47804878048780564, 0.48536585365853735, 0.492682926829269, 0.5000000000000007, 0.5073170731707324, 0.5146341463414641, 0.5219512195121957, 0.5292682926829274, 0.5365853658536591, 0.5439024390243908, 0.5512195121951224, 0.5585365853658542, 0.5658536585365859, 0.5731707317073175, 0.5804878048780492, 0.5878048780487809, 0.5951219512195126, 0.6024390243902442, 0.6097560975609759, 0.6170731707317076, 0.6243902439024392, 0.631707317073171, 0.6390243902439027]

    def test_phasor_6000Hz(self, phasor_list):
        res = phasor_list[2].get_block_of_samples()
        assert res == [0.0, 0.07317073170731707, 0.14634146341463414, 0.21951219512195122, 0.2926829268292683, 0.36585365853658536, 0.43902439024390244, 0.5121951219512195, 0.5853658536585367, 0.6585365853658537, 0.7317073170731708, 0.804878048780488, 0.878048780487805, 0.9512195121951221, 0.02439024390243922, 0.09756097560975628, 0.17073170731707335, 0.2439024390243904, 0.3170731707317075, 0.39024390243902457, 0.46341463414634165, 0.5365853658536588, 0.6097560975609758, 0.682926829268293, 0.7560975609756101, 0.8292682926829271, 0.9024390243902443, 0.9756097560975614, 0.04878048780487844, 0.12195121951219551, 0.19512195121951256, 0.2682926829268296, 0.3414634146341467, 0.4146341463414638, 0.48780487804878087, 0.560975609756098, 0.6341463414634151, 0.7073170731707322, 0.7804878048780493, 0.8536585365853664, 0.9268292682926834, 5.654319433712919e-16, 0.07317073170731764, 0.14634146341463472, 0.21951219512195178, 0.29268292682926883, 0.3658536585365859, 0.439024390243903, 0.5121951219512201, 0.5853658536585372, 0.6585365853658544, 0.7317073170731714, 0.8048780487804885, 0.8780487804878055, 0.9512195121951227, 0.024390243902439785, 0.09756097560975685, 0.1707317073170739, 0.24390243902439096, 0.31707317073170804, 0.3902439024390251, 0.4634146341463422, 0.5365853658536593, 0.6097560975609764, 0.6829268292682935, 0.7560975609756106, 0.8292682926829277, 0.9024390243902448, 0.975609756097562, 0.04878048780487901, 0.12195121951219606, 0.19512195121951312, 0.2682926829268302, 0.34146341463414726, 0.41463414634146434, 0.4878048780487815, 0.5609756097560985, 0.6341463414634156, 0.7073170731707328, 0.7804878048780498, 0.853658536585367, 0.9268292682926841, 1.1308638867425838e-15, 0.0731707317073182, 0.14634146341463528, 0.21951219512195236, 0.29268292682926944, 0.36585365853658647, 0.43902439024390355, 0.5121951219512206, 0.5853658536585378, 0.6585365853658549, 0.7317073170731719, 0.8048780487804891, 0.8780487804878061, 0.9512195121951232, 0.02439024390244035, 0.09756097560975742, 0.1707317073170745, 0.24390243902439154, 0.3170731707317086, 0.3902439024390257, 0.4634146341463428, 0.5365853658536599, 0.609756097560977, 0.6829268292682941, 0.7560975609756112, 0.8292682926829282, 0.9024390243902454, 0.9756097560975625, 0.04878048780487957, 0.12195121951219663, 0.1951219512195137, 0.2682926829268308, 0.3414634146341478, 0.4146341463414649, 0.48780487804878203, 0.5609756097560991, 0.6341463414634162, 0.7073170731707333, 0.7804878048780504, 0.8536585365853675, 0.9268292682926846, 1.6962958301138756e-15, 0.07317073170731876, 0.14634146341463583, 0.2195121951219529, 0.29268292682927, 0.365853658536587, 0.43902439024390416, 0.5121951219512212, 0.5853658536585383, 0.6585365853658555, 0.7317073170731725, 0.8048780487804896, 0.8780487804878068, 0.9512195121951238, 0.024390243902440916, 0.09756097560975797, 0.17073170731707504, 0.2439024390243921, 0.31707317073170915, 0.39024390243902624, 0.4634146341463434, 0.5365853658536605, 0.6097560975609776, 0.6829268292682946, 0.7560975609756118, 0.8292682926829289, 0.9024390243902459, 0.9756097560975631, 0.04878048780488014, 0.1219512195121972, 0.19512195121951426, 0.26829268292683134, 0.34146341463414837, 0.4146341463414655, 0.4878048780487826, 0.5609756097560997, 0.6341463414634168, 0.7073170731707339, 0.7804878048780509, 0.853658536585368, 0.9268292682926852, 2.2617277734851675e-15, 0.07317073170731933, 0.1463414634146364, 0.2195121951219535, 0.29268292682927055, 0.36585365853658763, 0.4390243902439047, 0.5121951219512219, 0.5853658536585389, 0.658536585365856, 0.731707317073173, 0.8048780487804902, 0.8780487804878073, 0.9512195121951244, 0.02439024390244148, 0.09756097560975854, 0.1707317073170756, 0.24390243902439268, 0.3170731707317097, 0.39024390243902685, 0.46341463414634393, 0.536585365853661, 0.6097560975609781, 0.6829268292682952, 0.7560975609756123, 0.8292682926829295, 0.9024390243902465, 0.9756097560975636, 0.0487804878048807, 0.12195121951219777, 0.19512195121951484, 0.2682926829268319, 0.341463414634149, 0.41463414634146606, 0.48780487804878314, 0.5609756097561003, 0.6341463414634173, 0.7073170731707344, 0.7804878048780516, 0.8536585365853686, 0.9268292682926857, 2.8271597168564595e-15, 0.0731707317073199, 0.14634146341463697, 0.21951219512195405, 0.2926829268292711, 0.3658536585365882, 0.43902439024390527, 0.5121951219512224, 0.5853658536585394, 0.6585365853658566, 0.7317073170731737, 0.8048780487804907, 0.8780487804878079, 0.9512195121951249, 0.024390243902442047, 0.09756097560975911, 0.17073170731707618, 0.24390243902439324, 0.3170731707317103, 0.3902439024390274]

    def test_phasor_60000Hz(self, phasor_list):
        res = phasor_list[3].get_block_of_samples()
        assert res == [0.0, 0.7317073170731707, 0.4634146341463414, 0.19512195121951206, 0.9268292682926828, 0.6585365853658535, 0.3902439024390241, 0.12195121951219483, 0.8536585365853655, 0.5853658536585362, 0.3170731707317069, 0.04878048780487759, 0.7804878048780483, 0.512195121951219, 0.24390243902438966, 0.9756097560975604, 0.707317073170731, 0.4390243902439017, 0.17073170731707243, 0.9024390243902431, 0.6341463414634138, 0.36585365853658447, 0.09756097560975519, 0.8292682926829259, 0.5609756097560966, 0.2926829268292673, 0.02439024390243795, 0.7560975609756087, 0.4878048780487793, 0.21951219512195003, 0.9512195121951207, 0.6829268292682914, 0.4146341463414621, 0.14634146341463278, 0.8780487804878034, 0.6097560975609742, 0.34146341463414487, 0.07317073170731554, 0.8048780487804862, 0.5365853658536569, 0.2682926829268276, 0.9999999999999983, 0.7317073170731689, 0.4634146341463397, 0.19512195121951037, 0.9268292682926811, 0.6585365853658518, 0.39024390243902246, 0.12195121951219313, 0.8536585365853638, 0.5853658536585346, 0.3170731707317052, 0.0487804878048759, 0.7804878048780466, 0.5121951219512173, 0.24390243902438796, 0.9756097560975586, 0.7073170731707293, 0.43902439024390005, 0.17073170731707074, 0.9024390243902414, 0.6341463414634121, 0.3658536585365828, 0.09756097560975349, 0.8292682926829242, 0.5609756097560948, 0.29268292682926556, 0.024390243902436253, 0.756097560975607, 0.48780487804877765, 0.21951219512194833, 0.951219512195119, 0.6829268292682897, 0.4146341463414604, 0.14634146341463108, 0.8780487804878018, 0.6097560975609725, 0.34146341463414315, 0.07317073170731385, 0.8048780487804845, 0.5365853658536552, 0.2682926829268259, 0.9999999999999966, 0.7317073170731673, 0.463414634146338, 0.19512195121950868, 0.9268292682926794, 0.65853658536585, 0.39024390243902074, 0.12195121951219144, 0.8536585365853622, 0.5853658536585328, 0.3170731707317035, 0.0487804878048742, 0.7804878048780449, 0.5121951219512156, 0.24390243902438627, 0.975609756097557, 0.7073170731707277, 0.43902439024389833, 0.17073170731706902, 0.9024390243902397, 0.6341463414634104, 0.3658536585365811, 0.0975609756097518, 0.8292682926829225, 0.5609756097560932, 0.2926829268292639, 0.024390243902434557, 0.7560975609756052, 0.4878048780487759, 0.21951219512194664, 0.9512195121951174, 0.682926829268288, 0.4146341463414587, 0.1463414634146294, 0.8780487804878001, 0.6097560975609708, 0.3414634146341415, 0.07317073170731216, 0.8048780487804829, 0.5365853658536536, 0.26829268292682423, 0.9999999999999949, 0.7317073170731656, 0.46341463414633627, 0.19512195121950698, 0.9268292682926776, 0.6585365853658484, 0.3902439024390191, 0.12195121951218975, 0.8536585365853604, 0.5853658536585311, 0.3170731707317018, 0.048780487804872506, 0.7804878048780431, 0.5121951219512139, 0.24390243902438458, 0.9756097560975553, 0.707317073170726, 0.43902439024389667, 0.17073170731706733, 0.902439024390238, 0.6341463414634088, 0.3658536585365794, 0.09756097560975009, 0.8292682926829208, 0.5609756097560915, 0.29268292682926217, 0.02439024390243286, 0.7560975609756035, 0.48780487804877426, 0.21951219512194492, 0.9512195121951156, 0.6829268292682863, 0.414634146341457, 0.1463414634146277, 0.8780487804877983, 0.609756097560969, 0.34146341463413976, 0.07317073170731045, 0.8048780487804812, 0.5365853658536518, 0.2682926829268225, 0.9999999999999932, 0.7317073170731639, 0.4634146341463346, 0.1951219512195053, 0.926829268292676, 0.6585365853658467, 0.39024390243901735, 0.12195121951218804, 0.8536585365853587, 0.5853658536585294, 0.3170731707317001, 0.048780487804870806, 0.7804878048780415, 0.5121951219512122, 0.24390243902438288, 0.9756097560975535, 0.7073170731707242, 0.43902439024389495, 0.17073170731706563, 0.9024390243902364, 0.634146341463407, 0.3658536585365777, 0.0975609756097484, 0.8292682926829191, 0.5609756097560897, 0.29268292682926045, 0.024390243902431163, 0.7560975609756019, 0.48780487804877254, 0.21951219512194323, 0.9512195121951139, 0.6829268292682846, 0.4146341463414553, 0.146341463414626, 0.8780487804877967, 0.6097560975609674, 0.34146341463413804, 0.07317073170730876, 0.8048780487804794, 0.5365853658536501, 0.26829268292682085, 0.9999999999999916, 0.7317073170731622, 0.4634146341463329, 0.1951219512195036, 0.9268292682926743, 0.6585365853658449, 0.39024390243901563, 0.12195121951218635, 0.8536585365853571, 0.5853658536585278, 0.31707317073169844, 0.04878048780486911, 0.7804878048780398, 0.5121951219512105, 0.2439024390243812, 0.9756097560975519, 0.7073170731707226, 0.4390243902438933, 0.17073170731706394, 0.9024390243902346]
