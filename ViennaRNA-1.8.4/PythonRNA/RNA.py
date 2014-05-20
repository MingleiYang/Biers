# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.31
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _RNA
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


new_intP = _RNA.new_intP
delete_intP = _RNA.delete_intP
intP_getitem = _RNA.intP_getitem
intP_setitem = _RNA.intP_setitem
class intArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, intArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, intArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _RNA.new_intArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _RNA.delete_intArray
    __del__ = lambda self : None;
    def __getitem__(*args): return _RNA.intArray___getitem__(*args)
    def __setitem__(*args): return _RNA.intArray___setitem__(*args)
    def cast(*args): return _RNA.intArray_cast(*args)
    __swig_getmethods__["frompointer"] = lambda x: _RNA.intArray_frompointer
    if _newclass:frompointer = staticmethod(_RNA.intArray_frompointer)
intArray_swigregister = _RNA.intArray_swigregister
intArray_swigregister(intArray)
intArray_frompointer = _RNA.intArray_frompointer

new_floatP = _RNA.new_floatP
delete_floatP = _RNA.delete_floatP
floatP_getitem = _RNA.floatP_getitem
floatP_setitem = _RNA.floatP_setitem
class floatArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, floatArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, floatArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _RNA.new_floatArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _RNA.delete_floatArray
    __del__ = lambda self : None;
    def __getitem__(*args): return _RNA.floatArray___getitem__(*args)
    def __setitem__(*args): return _RNA.floatArray___setitem__(*args)
    def cast(*args): return _RNA.floatArray_cast(*args)
    __swig_getmethods__["frompointer"] = lambda x: _RNA.floatArray_frompointer
    if _newclass:frompointer = staticmethod(_RNA.floatArray_frompointer)
floatArray_swigregister = _RNA.floatArray_swigregister
floatArray_swigregister(floatArray)
floatArray_frompointer = _RNA.floatArray_frompointer

new_doubleP = _RNA.new_doubleP
delete_doubleP = _RNA.delete_doubleP
doubleP_getitem = _RNA.doubleP_getitem
doubleP_setitem = _RNA.doubleP_setitem
class doubleArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, doubleArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, doubleArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _RNA.new_doubleArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _RNA.delete_doubleArray
    __del__ = lambda self : None;
    def __getitem__(*args): return _RNA.doubleArray___getitem__(*args)
    def __setitem__(*args): return _RNA.doubleArray___setitem__(*args)
    def cast(*args): return _RNA.doubleArray_cast(*args)
    __swig_getmethods__["frompointer"] = lambda x: _RNA.doubleArray_frompointer
    if _newclass:frompointer = staticmethod(_RNA.doubleArray_frompointer)
doubleArray_swigregister = _RNA.doubleArray_swigregister
doubleArray_swigregister(doubleArray)
doubleArray_frompointer = _RNA.doubleArray_frompointer

new_ushortP = _RNA.new_ushortP
delete_ushortP = _RNA.delete_ushortP
ushortP_getitem = _RNA.ushortP_getitem
ushortP_setitem = _RNA.ushortP_setitem
new_shortP = _RNA.new_shortP
delete_shortP = _RNA.delete_shortP
shortP_getitem = _RNA.shortP_getitem
shortP_setitem = _RNA.shortP_setitem
cdata = _RNA.cdata
memmove = _RNA.memmove
VERSION = _RNA.VERSION
fold = _RNA.fold
energy_of_struct = _RNA.energy_of_struct
free_arrays = _RNA.free_arrays
initialize_fold = _RNA.initialize_fold
update_fold_params = _RNA.update_fold_params
backtrack_fold_from_pair = _RNA.backtrack_fold_from_pair
loop_energy = _RNA.loop_energy
export_fold_arrays = _RNA.export_fold_arrays
circfold = _RNA.circfold
energy_of_circ_struct = _RNA.energy_of_circ_struct
export_circfold_arrays = _RNA.export_circfold_arrays
load_experimental_data = _RNA.load_experimental_data
cofold = _RNA.cofold
free_co_arrays = _RNA.free_co_arrays
initialize_cofold = _RNA.initialize_cofold
update_cofold_params = _RNA.update_cofold_params
zukersubopt = _RNA.zukersubopt
pf_fold = _RNA.pf_fold
init_pf_fold = _RNA.init_pf_fold
free_pf_arrays = _RNA.free_pf_arrays
update_pf_params = _RNA.update_pf_params
bppm_symbol = _RNA.bppm_symbol
mean_bp_dist = _RNA.mean_bp_dist
centroid = _RNA.centroid
get_pf_arrays = _RNA.get_pf_arrays
pbacktrack = _RNA.pbacktrack
pf_circ_fold = _RNA.pf_circ_fold
pbacktrack_circ = _RNA.pbacktrack_circ
load_pf_experimental_data = _RNA.load_pf_experimental_data
co_pf_fold = _RNA.co_pf_fold
free_co_pf_arrays = _RNA.free_co_pf_arrays
update_co_pf_params = _RNA.update_co_pf_params
inverse_fold = _RNA.inverse_fold
inverse_pf_fold = _RNA.inverse_pf_fold
class bondT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, bondT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, bondT, name)
    __repr__ = _swig_repr
    __swig_setmethods__["i"] = _RNA.bondT_i_set
    __swig_getmethods__["i"] = _RNA.bondT_i_get
    if _newclass:i = _swig_property(_RNA.bondT_i_get, _RNA.bondT_i_set)
    __swig_setmethods__["j"] = _RNA.bondT_j_set
    __swig_getmethods__["j"] = _RNA.bondT_j_get
    if _newclass:j = _swig_property(_RNA.bondT_j_get, _RNA.bondT_j_set)
    def get(*args): return _RNA.bondT_get(*args)
    def __init__(self, *args): 
        this = _RNA.new_bondT(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _RNA.delete_bondT
    __del__ = lambda self : None;
bondT_swigregister = _RNA.bondT_swigregister
bondT_swigregister(bondT)
cvar = _RNA.cvar
get_concentrations = _RNA.get_concentrations

option_string = _RNA.option_string
free_alifold_arrays = _RNA.free_alifold_arrays
class pair_info(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pair_info, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pair_info, name)
    __repr__ = _swig_repr
    __swig_setmethods__["i"] = _RNA.pair_info_i_set
    __swig_getmethods__["i"] = _RNA.pair_info_i_get
    if _newclass:i = _swig_property(_RNA.pair_info_i_get, _RNA.pair_info_i_set)
    __swig_setmethods__["j"] = _RNA.pair_info_j_set
    __swig_getmethods__["j"] = _RNA.pair_info_j_get
    if _newclass:j = _swig_property(_RNA.pair_info_j_get, _RNA.pair_info_j_set)
    __swig_setmethods__["p"] = _RNA.pair_info_p_set
    __swig_getmethods__["p"] = _RNA.pair_info_p_get
    if _newclass:p = _swig_property(_RNA.pair_info_p_get, _RNA.pair_info_p_set)
    __swig_setmethods__["ent"] = _RNA.pair_info_ent_set
    __swig_getmethods__["ent"] = _RNA.pair_info_ent_get
    if _newclass:ent = _swig_property(_RNA.pair_info_ent_get, _RNA.pair_info_ent_set)
    __swig_setmethods__["bp"] = _RNA.pair_info_bp_set
    __swig_getmethods__["bp"] = _RNA.pair_info_bp_get
    if _newclass:bp = _swig_property(_RNA.pair_info_bp_get, _RNA.pair_info_bp_set)
    __swig_setmethods__["comp"] = _RNA.pair_info_comp_set
    __swig_getmethods__["comp"] = _RNA.pair_info_comp_get
    if _newclass:comp = _swig_property(_RNA.pair_info_comp_get, _RNA.pair_info_comp_set)
    def __init__(self, *args): 
        this = _RNA.new_pair_info(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _RNA.delete_pair_info
    __del__ = lambda self : None;
pair_info_swigregister = _RNA.pair_info_swigregister
pair_info_swigregister(pair_info)

alipf_fold = _RNA.alipf_fold
centroid_ali = _RNA.centroid_ali
readribosum = _RNA.readribosum
alipbacktrack = _RNA.alipbacktrack
free_alipf_arrays = _RNA.free_alipf_arrays
energy_of_alistruct = _RNA.energy_of_alistruct
circalifold = _RNA.circalifold
alipf_circ_fold = _RNA.alipf_circ_fold
alifold = _RNA.alifold
consensus = _RNA.consensus
consens_mis = _RNA.consens_mis
class COORDINATE(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, COORDINATE, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, COORDINATE, name)
    __repr__ = _swig_repr
    __swig_setmethods__["X"] = _RNA.COORDINATE_X_set
    __swig_getmethods__["X"] = _RNA.COORDINATE_X_get
    if _newclass:X = _swig_property(_RNA.COORDINATE_X_get, _RNA.COORDINATE_X_set)
    __swig_setmethods__["Y"] = _RNA.COORDINATE_Y_set
    __swig_getmethods__["Y"] = _RNA.COORDINATE_Y_get
    if _newclass:Y = _swig_property(_RNA.COORDINATE_Y_get, _RNA.COORDINATE_Y_set)
    def get(*args): return _RNA.COORDINATE_get(*args)
    def __init__(self, *args): 
        this = _RNA.new_COORDINATE(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _RNA.delete_COORDINATE
    __del__ = lambda self : None;
COORDINATE_swigregister = _RNA.COORDINATE_swigregister
COORDINATE_swigregister(COORDINATE)

get_xy_coordinates = _RNA.get_xy_coordinates
class SOLUTION(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SOLUTION, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SOLUTION, name)
    __repr__ = _swig_repr
    __swig_setmethods__["energy"] = _RNA.SOLUTION_energy_set
    __swig_getmethods__["energy"] = _RNA.SOLUTION_energy_get
    if _newclass:energy = _swig_property(_RNA.SOLUTION_energy_get, _RNA.SOLUTION_energy_set)
    __swig_setmethods__["structure"] = _RNA.SOLUTION_structure_set
    __swig_getmethods__["structure"] = _RNA.SOLUTION_structure_get
    if _newclass:structure = _swig_property(_RNA.SOLUTION_structure_get, _RNA.SOLUTION_structure_set)
    def get(*args): return _RNA.SOLUTION_get(*args)
    def size(*args): return _RNA.SOLUTION_size(*args)
    __swig_destroy__ = _RNA.delete_SOLUTION
    __del__ = lambda self : None;
    def __init__(self, *args): 
        this = _RNA.new_SOLUTION(*args)
        try: self.this.append(this)
        except: self.this = this
SOLUTION_swigregister = _RNA.SOLUTION_swigregister
SOLUTION_swigregister(SOLUTION)

subopt = _RNA.subopt
get_pr = _RNA.get_pr
b2HIT = _RNA.b2HIT
b2C = _RNA.b2C
b2Shapiro = _RNA.b2Shapiro
add_root = _RNA.add_root
expand_Shapiro = _RNA.expand_Shapiro
expand_Full = _RNA.expand_Full
unexpand_Full = _RNA.unexpand_Full
unweight = _RNA.unweight
unexpand_aligned_F = _RNA.unexpand_aligned_F
parse_structure = _RNA.parse_structure
make_tree = _RNA.make_tree
tree_edit_distance = _RNA.tree_edit_distance
print_tree = _RNA.print_tree
free_tree = _RNA.free_tree
Make_swString = _RNA.Make_swString
string_edit_distance = _RNA.string_edit_distance
Make_bp_profile = _RNA.Make_bp_profile
profile_edit_distance = _RNA.profile_edit_distance
print_bppm = _RNA.print_bppm
free_profile = _RNA.free_profile
space = _RNA.space
xrealloc = _RNA.xrealloc
nrerror = _RNA.nrerror
init_rand = _RNA.init_rand
urn = _RNA.urn
int_urn = _RNA.int_urn
filecopy = _RNA.filecopy
time_stamp = _RNA.time_stamp
random_string = _RNA.random_string
hamming = _RNA.hamming
get_line = _RNA.get_line
pack_structure = _RNA.pack_structure
unpack_structure = _RNA.unpack_structure
make_pair_table = _RNA.make_pair_table
bp_distance = _RNA.bp_distance
read_parameter_file = _RNA.read_parameter_file
write_parameter_file = _RNA.write_parameter_file
deref_any = _RNA.deref_any
scale_parameters = _RNA.scale_parameters
copy_parameters = _RNA.copy_parameters
set_parameters = _RNA.set_parameters
get_aligned_line = _RNA.get_aligned_line
make_loop_index = _RNA.make_loop_index
energy_of_move = _RNA.energy_of_move
class duplexT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, duplexT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, duplexT, name)
    __repr__ = _swig_repr
    __swig_setmethods__["i"] = _RNA.duplexT_i_set
    __swig_getmethods__["i"] = _RNA.duplexT_i_get
    if _newclass:i = _swig_property(_RNA.duplexT_i_get, _RNA.duplexT_i_set)
    __swig_setmethods__["j"] = _RNA.duplexT_j_set
    __swig_getmethods__["j"] = _RNA.duplexT_j_get
    if _newclass:j = _swig_property(_RNA.duplexT_j_get, _RNA.duplexT_j_set)
    __swig_setmethods__["structure"] = _RNA.duplexT_structure_set
    __swig_getmethods__["structure"] = _RNA.duplexT_structure_get
    if _newclass:structure = _swig_property(_RNA.duplexT_structure_get, _RNA.duplexT_structure_set)
    __swig_setmethods__["energy"] = _RNA.duplexT_energy_set
    __swig_getmethods__["energy"] = _RNA.duplexT_energy_get
    if _newclass:energy = _swig_property(_RNA.duplexT_energy_get, _RNA.duplexT_energy_set)
    def __init__(self, *args): 
        this = _RNA.new_duplexT(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _RNA.delete_duplexT
    __del__ = lambda self : None;
duplexT_swigregister = _RNA.duplexT_swigregister
duplexT_swigregister(duplexT)

duplexfold = _RNA.duplexfold
aliduplexfold = _RNA.aliduplexfold
encode_seq = _RNA.encode_seq
Lfold = _RNA.Lfold
PS_rna_plot = _RNA.PS_rna_plot
PS_rna_plot_a = _RNA.PS_rna_plot_a
gmlRNA = _RNA.gmlRNA
ssv_rna_plot = _RNA.ssv_rna_plot
svg_rna_plot = _RNA.svg_rna_plot
xrna_plot = _RNA.xrna_plot
PS_dot_plot = _RNA.PS_dot_plot
class cpair(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cpair, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cpair, name)
    __repr__ = _swig_repr
    __swig_setmethods__["i"] = _RNA.cpair_i_set
    __swig_getmethods__["i"] = _RNA.cpair_i_get
    if _newclass:i = _swig_property(_RNA.cpair_i_get, _RNA.cpair_i_set)
    __swig_setmethods__["j"] = _RNA.cpair_j_set
    __swig_getmethods__["j"] = _RNA.cpair_j_get
    if _newclass:j = _swig_property(_RNA.cpair_j_get, _RNA.cpair_j_set)
    __swig_setmethods__["mfe"] = _RNA.cpair_mfe_set
    __swig_getmethods__["mfe"] = _RNA.cpair_mfe_get
    if _newclass:mfe = _swig_property(_RNA.cpair_mfe_get, _RNA.cpair_mfe_set)
    __swig_setmethods__["p"] = _RNA.cpair_p_set
    __swig_getmethods__["p"] = _RNA.cpair_p_get
    if _newclass:p = _swig_property(_RNA.cpair_p_get, _RNA.cpair_p_set)
    __swig_setmethods__["hue"] = _RNA.cpair_hue_set
    __swig_getmethods__["hue"] = _RNA.cpair_hue_get
    if _newclass:hue = _swig_property(_RNA.cpair_hue_get, _RNA.cpair_hue_set)
    __swig_setmethods__["sat"] = _RNA.cpair_sat_set
    __swig_getmethods__["sat"] = _RNA.cpair_sat_get
    if _newclass:sat = _swig_property(_RNA.cpair_sat_get, _RNA.cpair_sat_set)
    def __init__(self, *args): 
        this = _RNA.new_cpair(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _RNA.delete_cpair
    __del__ = lambda self : None;
cpair_swigregister = _RNA.cpair_swigregister
cpair_swigregister(cpair)

PS_color_dot_plot = _RNA.PS_color_dot_plot
PS_color_dot_plot_turn = _RNA.PS_color_dot_plot_turn
class plist(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, plist, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, plist, name)
    __repr__ = _swig_repr
    __swig_setmethods__["i"] = _RNA.plist_i_set
    __swig_getmethods__["i"] = _RNA.plist_i_get
    if _newclass:i = _swig_property(_RNA.plist_i_get, _RNA.plist_i_set)
    __swig_setmethods__["j"] = _RNA.plist_j_set
    __swig_getmethods__["j"] = _RNA.plist_j_get
    if _newclass:j = _swig_property(_RNA.plist_j_get, _RNA.plist_j_set)
    __swig_setmethods__["p"] = _RNA.plist_p_set
    __swig_getmethods__["p"] = _RNA.plist_p_get
    if _newclass:p = _swig_property(_RNA.plist_p_get, _RNA.plist_p_set)
    def __init__(self, *args): 
        this = _RNA.new_plist(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _RNA.delete_plist
    __del__ = lambda self : None;
plist_swigregister = _RNA.plist_swigregister
plist_swigregister(plist)

PS_dot_plot_list = _RNA.PS_dot_plot_list
PS_dot_plot_turn = _RNA.PS_dot_plot_turn
PS_color_aln = _RNA.PS_color_aln
class path_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, path_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, path_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["en"] = _RNA.path_t_en_set
    __swig_getmethods__["en"] = _RNA.path_t_en_get
    if _newclass:en = _swig_property(_RNA.path_t_en_get, _RNA.path_t_en_set)
    __swig_setmethods__["s"] = _RNA.path_t_s_set
    __swig_getmethods__["s"] = _RNA.path_t_s_get
    if _newclass:s = _swig_property(_RNA.path_t_s_get, _RNA.path_t_s_set)
    def __init__(self, *args): 
        this = _RNA.new_path_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _RNA.delete_path_t
    __del__ = lambda self : None;
path_t_swigregister = _RNA.path_t_swigregister
path_t_swigregister(path_t)

find_saddle = _RNA.find_saddle
get_path = _RNA.get_path


