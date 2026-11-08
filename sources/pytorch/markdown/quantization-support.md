Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/quantization-support.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/quantization-support.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/quantization-support.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/quantization-support.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/quantization-support.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/quantization-support.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/quantization-support.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/quantization-support.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/quantization-support.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/quantization-support.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/quantization-support.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/quantization-support.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/quantization-support.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/quantization-support.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/quantization-support.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/quantization-support.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/quantization-support.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/quantization-support.html)
[v1.13](https://docs.pytorch.org/docs/1.13/quantization-support.html)
[v1.12](https://docs.pytorch.org/docs/1.12/quantization-support.html)
[v1.11](https://docs.pytorch.org/docs/1.11/quantization-support.html)
[v1.10](https://docs.pytorch.org/docs/1.10/quantization-support.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/quantization-support.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/quantization-support.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/quantization-support.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/quantization-support.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/quantization-support.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/quantization-support.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/quantization-support.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/quantization-support.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/quantization-support.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/quantization-support.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/quantization-support.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/quantization-support.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/quantization-support.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/quantization-support.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/quantization-support.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/quantization-support.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/quantization-support.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/quantization-support.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/quantization-support.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/quantization-support.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/quantization-support.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/quantization-support.html)

[Go to pytorch.org](https://pytorch.org/)

 Ctrl+K

|     |     |
| --- | --- |
|     | [×](javascript:void(0) "Clear search box") |

search

Custom Search

|     |     |
| --- | --- |
|     | Sort by<br><br>Relevance<br><br>Date |

*   [X](https://x.com/PyTorch)
    
*   [GitHub](https://github.com/pytorch/pytorch)
    
*   [PyTorch Forum](https://discuss.pytorch.org/)
    
*   [PyPi](https://pypi.org/project/torch/)
    

Rate this Page

★ ★ ★ ★ ★

Quantization API Reference[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#quantization-api-reference "Link to this heading")

==============================================================================================================================================

Created On: Jul 25, 2020 | Last Updated On: May 11, 2026

torch.ao.quantization[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#torch-ao-quantization "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

This module contains Eager mode quantization APIs.

### Top level APIs[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#top-level-apis "Link to this heading")

|     |     |
| --- | --- |
| [`quantize`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantize.html#torch.ao.quantization.quantize "torch.ao.quantization.quantize") | Quantize the input float model with post training static quantization. |
| [`quantize_dynamic`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantize_dynamic.html#torch.ao.quantization.quantize_dynamic "torch.ao.quantization.quantize_dynamic") | Converts a float model to dynamic (i.e. weights-only) quantized model. |
| [`quantize_qat`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantize_qat.html#torch.ao.quantization.quantize_qat "torch.ao.quantization.quantize_qat") | Do quantization aware training and output a quantized model |
| [`prepare`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.prepare.html#torch.ao.quantization.prepare "torch.ao.quantization.prepare") | Prepares a copy of the model for quantization calibration or quantization-aware training. |
| [`prepare_qat`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.prepare_qat.html#torch.ao.quantization.prepare_qat "torch.ao.quantization.prepare_qat") | Prepares a copy of the model for quantization calibration or quantization-aware training and converts it to quantized version. |
| [`convert`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.convert.html#torch.ao.quantization.convert "torch.ao.quantization.convert") | Converts submodules in input module to a different module according to mapping by calling from\_float method on the target module class. |

### Preparing model for quantization[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#preparing-model-for-quantization "Link to this heading")

|     |     |
| --- | --- |
| [`fuse_modules.fuse_modules`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fuse_modules.fuse_modules.html#torch.ao.quantization.fuse_modules.fuse_modules "torch.ao.quantization.fuse_modules.fuse_modules") | Fuse a list of modules into a single module. |
| [`QuantStub`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.QuantStub.html#torch.ao.quantization.QuantStub "torch.ao.quantization.QuantStub") | Quantize stub module, before calibration, this is same as an observer, it will be swapped as nnq.Quantize in convert. |
| [`DeQuantStub`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.DeQuantStub.html#torch.ao.quantization.DeQuantStub "torch.ao.quantization.DeQuantStub") | Dequantize stub module, before calibration, this is same as identity, this will be swapped as nnq.DeQuantize in convert. |
| [`QuantWrapper`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.QuantWrapper.html#torch.ao.quantization.QuantWrapper "torch.ao.quantization.QuantWrapper") | A wrapper class that wraps the input module, adds QuantStub and DeQuantStub and surrounds the call to module with call to quant and dequant modules. |
| [`add_quant_dequant`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.add_quant_dequant.html#torch.ao.quantization.add_quant_dequant "torch.ao.quantization.add_quant_dequant") | Wrap the leaf child module in QuantWrapper if it has a valid qconfig Note that this function will modify the children of module inplace and it can return a new module which wraps the input module as well. |

### Utility functions[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#utility-functions "Link to this heading")

|     |     |
| --- | --- |
| [`ObserverOrFakeQuantize`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.ObserverOrFakeQuantize.html#torch.ao.quantization.ObserverOrFakeQuantize "torch.ao.quantization.ObserverOrFakeQuantize") | Create named, parameterized type aliases. |
| [`swap_module`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.swap_module.html#torch.ao.quantization.swap_module "torch.ao.quantization.swap_module") | Swaps the module if it has a quantized counterpart and it has an observer attached. |
| [`propagate_qconfig_`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.propagate_qconfig_.html#torch.ao.quantization.propagate_qconfig_ "torch.ao.quantization.propagate_qconfig_") | Propagate qconfig through the module hierarchy and assign qconfig attribute on each leaf module |
| [`default_eval_fn`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.default_eval_fn.html#torch.ao.quantization.default_eval_fn "torch.ao.quantization.default_eval_fn") | Define the default evaluation function. |

torch.ao.quantization.utils[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#module-torch.ao.quantization.utils "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

Utils shared by different modes of quantization (eager/graph)

|     |     |
| --- | --- |
| [`activation_is_dynamically_quantized`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.utils.activation_is_dynamically_quantized.html#torch.ao.quantization.utils.activation_is_dynamically_quantized "torch.ao.quantization.utils.activation_is_dynamically_quantized") | Given a qconfig, decide if the activation needs to be dynamically quantized or not, this includes dynamically quantizing to quint8, qint8 and float16 |
| [`activation_is_int32_quantized`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.utils.activation_is_int32_quantized.html#torch.ao.quantization.utils.activation_is_int32_quantized "torch.ao.quantization.utils.activation_is_int32_quantized") | Given a qconfig, decide if the activation needs to be quantized to int32 or not |
| [`activation_is_int8_quantized`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.utils.activation_is_int8_quantized.html#torch.ao.quantization.utils.activation_is_int8_quantized "torch.ao.quantization.utils.activation_is_int8_quantized") | Given a qconfig, decide if the activation needs to be quantized to int8 or not, this includes quantizing to quint8, qint8 |
| [`activation_is_statically_quantized`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.utils.activation_is_statically_quantized.html#torch.ao.quantization.utils.activation_is_statically_quantized "torch.ao.quantization.utils.activation_is_statically_quantized") | Given a qconfig, decide if the activation needs to be quantized or not, this includes quantizing to quint8, qint8 and qint32 and float16 |
| [`calculate_qmin_qmax`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.utils.calculate_qmin_qmax.html#torch.ao.quantization.utils.calculate_qmin_qmax "torch.ao.quantization.utils.calculate_qmin_qmax") | Calculates actual qmin and qmax based on the quantization range, observer datatype and if range is reduced. |
| [`check_min_max_valid`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.utils.check_min_max_valid.html#torch.ao.quantization.utils.check_min_max_valid "torch.ao.quantization.utils.check_min_max_valid") | Checks if the given minimum and maximum values are valid, meaning that they exist and the min value is less than the max value. |
| [`determine_qparams`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.utils.determine_qparams.html#torch.ao.quantization.utils.determine_qparams "torch.ao.quantization.utils.determine_qparams") | Calculates the quantization parameters, given min and max value tensors. |
| [`get_combined_dict`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.utils.get_combined_dict.html#torch.ao.quantization.utils.get_combined_dict "torch.ao.quantization.utils.get_combined_dict") | Combines two dictionaries. |
| [`get_fqn_to_example_inputs`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.utils.get_fqn_to_example_inputs.html#torch.ao.quantization.utils.get_fqn_to_example_inputs "torch.ao.quantization.utils.get_fqn_to_example_inputs") | Given a model and its example inputs, return a dictionary from fully qualified name of submodules to example\_inputs for that submodule, e.g. `{"linear1": (tensor1,), "linear2": (tensor2,), "sub": (tensor3,), "sub.linear1": (tensor4,), ...}`. |
| [`get_qconfig_dtypes`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.utils.get_qconfig_dtypes.html#torch.ao.quantization.utils.get_qconfig_dtypes "torch.ao.quantization.utils.get_qconfig_dtypes") | returns the qconfig tuple for qconfig: (activation\_dtype, weight\_dtype, activation\_is\_dynamic) |
| [`get_qparam_dict`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.utils.get_qparam_dict.html#torch.ao.quantization.utils.get_qparam_dict "torch.ao.quantization.utils.get_qparam_dict") |     |
| [`get_quant_type`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.utils.get_quant_type.html#torch.ao.quantization.utils.get_quant_type "torch.ao.quantization.utils.get_quant_type") |     |
| [`get_swapped_custom_module_class`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.utils.get_swapped_custom_module_class.html#torch.ao.quantization.utils.get_swapped_custom_module_class "torch.ao.quantization.utils.get_swapped_custom_module_class") | Get the observed/quantized custom module class that we need to swap `custom_module` to. |
| [`getattr_from_fqn`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.utils.getattr_from_fqn.html#torch.ao.quantization.utils.getattr_from_fqn "torch.ao.quantization.utils.getattr_from_fqn") | Given an obj and a fqn such as "foo.bar.baz", returns gm.foo.bar.baz. |
| [`NodePattern`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.utils.NodePattern.html#torch.ao.quantization.utils.NodePattern "torch.ao.quantization.utils.NodePattern") | Create named, parameterized type aliases. |
| [`Pattern`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.utils.Pattern.html#torch.ao.quantization.utils.Pattern "torch.ao.quantization.utils.Pattern") | Create named, parameterized type aliases. |
| [`validate_qmin_qmax`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.utils.validate_qmin_qmax.html#torch.ao.quantization.utils.validate_qmin_qmax "torch.ao.quantization.utils.validate_qmin_qmax") | Validates that the user-specified quantization range is properly initialized and within the given bound supported by the observer dtype. |

torch.ao.quantization.quantize\_fx[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#torch-ao-quantization-quantize-fx "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

This module contains FX graph mode quantization APIs (prototype).

torch.ao.quantization.quantize\_fx.attach\_preserved\_attrs\_to\_model(_model_, _preserved\_attrs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/ao/quantization/quantize_fx.py#L25)
[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#torch.ao.quantization.quantize_fx.attach_preserved_attrs_to_model "Link to this definition")

Store preserved attributes to the model.meta so that it can be preserved during deepcopy

torch.ao.quantization.quantize\_fx.convert\_to\_reference\_fx(_graph\_module_, _convert\_custom\_config\=None_, _\_remove\_qconfig\=True_, _qconfig\_mapping\=None_, _backend\_config\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/ao/quantization/quantize_fx.py#L636)
[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#torch.ao.quantization.quantize_fx.convert_to_reference_fx "Link to this definition")

Convert a calibrated or trained model to a reference quantized model, see [pytorch/rfcs](https://github.com/pytorch/rfcs/blob/master/RFC-0019-Extending-PyTorch-Quantization-to-Custom-Backends.md)
 for more details, reference quantized model is a standard representation of a quantized model provided by FX Graph Mode Quantization, it can be further lowered to run on the target hardware, like accelerators

Parameters:

*   **graph\_module** (_\*_) – A prepared and calibrated/trained model (GraphModule)
    
*   **convert\_custom\_config** (_\*_) – custom configurations for convert function. See [`convert_fx()`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantize_fx.convert_fx.html#torch.ao.quantization.quantize_fx.convert_fx "torch.ao.quantization.quantize_fx.convert_fx")
     for more details.
    
*   **\_remove\_qconfig** (_\*_) – Option to remove the qconfig attributes in the model after convert.
    
*   **qconfig\_mapping** (_\*_) –
    
    config for specifying how to convert a model for quantization.
    
    See [`convert_fx()`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantize_fx.convert_fx.html#torch.ao.quantization.quantize_fx.convert_fx "torch.ao.quantization.quantize_fx.convert_fx")
     for more details.
    
    *   backend\_config (BackendConfig): A configuration for the backend which describes how
        
        operators should be quantized in the backend. See [`convert_fx()`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantize_fx.convert_fx.html#torch.ao.quantization.quantize_fx.convert_fx "torch.ao.quantization.quantize_fx.convert_fx")
         for more details.
        
    

Returns:

A reference quantized model (GraphModule)

Return type:

[_GraphModule_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule "torch.fx.graph_module.GraphModule")

Example:

\# prepared\_model: the model after prepare\_fx/prepare\_qat\_fx and calibration/training
\# TODO: add backend\_config after we split the backend\_config for fbgemm and qnnpack
\# e.g. backend\_config = get\_default\_backend\_config("fbgemm")
reference\_quantized\_model \= convert\_to\_reference\_fx(prepared\_model)

Copy to clipboard

|     |     |
| --- | --- |
| [`prepare_fx`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantize_fx.prepare_fx.html#torch.ao.quantization.quantize_fx.prepare_fx "torch.ao.quantization.quantize_fx.prepare_fx") | Prepare a model for post training quantization |
| [`prepare_qat_fx`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantize_fx.prepare_qat_fx.html#torch.ao.quantization.quantize_fx.prepare_qat_fx "torch.ao.quantization.quantize_fx.prepare_qat_fx") | Prepare a model for quantization aware training |
| [`convert_fx`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantize_fx.convert_fx.html#torch.ao.quantization.quantize_fx.convert_fx "torch.ao.quantization.quantize_fx.convert_fx") | Convert a calibrated or trained model to a quantized model |
| [`fuse_fx`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantize_fx.fuse_fx.html#torch.ao.quantization.quantize_fx.fuse_fx "torch.ao.quantization.quantize_fx.fuse_fx") | Fuse modules like conv+bn, conv+bn+relu etc, model must be in eval mode. |

torch.ao.quantization.qconfig\_mapping[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#torch-ao-quantization-qconfig-mapping "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

This module contains QConfigMapping for configuring FX graph mode quantization.

|     |     |
| --- | --- |
| [`QConfigMapping`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.qconfig_mapping.QConfigMapping.html#torch.ao.quantization.qconfig_mapping.QConfigMapping "torch.ao.quantization.qconfig_mapping.QConfigMapping") | Mapping from model ops to `torch.ao.quantization.QConfig` s. |
| [`get_default_qconfig_mapping`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.qconfig_mapping.get_default_qconfig_mapping.html#torch.ao.quantization.qconfig_mapping.get_default_qconfig_mapping "torch.ao.quantization.qconfig_mapping.get_default_qconfig_mapping") | Return the default QConfigMapping for post training quantization. |
| [`get_default_qat_qconfig_mapping`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.qconfig_mapping.get_default_qat_qconfig_mapping.html#torch.ao.quantization.qconfig_mapping.get_default_qat_qconfig_mapping "torch.ao.quantization.qconfig_mapping.get_default_qat_qconfig_mapping") | Return the default QConfigMapping for quantization aware training. |

torch.ao.quantization.backend\_config[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#torch-ao-quantization-backend-config "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

This module contains BackendConfig, a config object that defines how quantization is supported in a backend. Currently only used by FX Graph Mode Quantization, but we may extend Eager Mode Quantization to work with this as well.

|     |     |
| --- | --- |
| [`BackendConfig`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.backend_config.BackendConfig.html#torch.ao.quantization.backend_config.BackendConfig "torch.ao.quantization.backend_config.BackendConfig") | Config that defines the set of patterns that can be quantized on a given backend, and how reference quantized models can be produced from these patterns. |
| [`BackendPatternConfig`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.backend_config.BackendPatternConfig.html#torch.ao.quantization.backend_config.BackendPatternConfig "torch.ao.quantization.backend_config.BackendPatternConfig") | Config object that specifies quantization behavior for a given operator pattern. |
| [`DTypeConfig`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.backend_config.DTypeConfig.html#torch.ao.quantization.backend_config.DTypeConfig "torch.ao.quantization.backend_config.DTypeConfig") | Config object that specifies the supported data types passed as arguments to quantize ops in the reference model spec, for input and output activations, weights, and biases. |
| [`DTypeWithConstraints`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.backend_config.DTypeWithConstraints.html#torch.ao.quantization.backend_config.DTypeWithConstraints "torch.ao.quantization.backend_config.DTypeWithConstraints") | Config for specifying additional constraints for a given dtype, such as quantization value ranges, scale value ranges, and fixed quantization params, to be used in [`DTypeConfig`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.backend_config.DTypeConfig.html#torch.ao.quantization.backend_config.DTypeConfig "torch.ao.quantization.backend_config.DTypeConfig")<br>. |
| [`ObservationType`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.backend_config.ObservationType.html#torch.ao.quantization.backend_config.ObservationType "torch.ao.quantization.backend_config.ObservationType") | An enum that represents different ways of how an operator/operator pattern should be observed |

torch.ao.quantization.backend\_config.executorch.get\_executorch\_backend\_config()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/ao/quantization/backend_config/executorch.py#L485)
[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#torch.ao.quantization.backend_config.executorch.get_executorch_backend_config "Link to this definition")

Return the BackendConfig for backends PyTorch lowers to through the Executorch stack.

Return type:

[_BackendConfig_](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.backend_config.BackendConfig.html#torch.ao.quantization.backend_config.BackendConfig "torch.ao.quantization.backend_config.backend_config.BackendConfig")

torch.ao.quantization.backend\_config.fbgemm.get\_fbgemm\_backend\_config()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/ao/quantization/backend_config/fbgemm.py#L85)
[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#torch.ao.quantization.backend_config.fbgemm.get_fbgemm_backend_config "Link to this definition")

Return the BackendConfig for PyTorch’s native FBGEMM backend.

Return type:

[_BackendConfig_](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.backend_config.BackendConfig.html#torch.ao.quantization.backend_config.BackendConfig "torch.ao.quantization.backend_config.backend_config.BackendConfig")

torch.ao.quantization.backend\_config.onednn.get\_onednn\_backend\_config()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/ao/quantization/backend_config/onednn.py#L613)
[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#torch.ao.quantization.backend_config.onednn.get_onednn_backend_config "Link to this definition")

Return the BackendConfig for PyTorch’s native ONEDNN backend.

Return type:

[_BackendConfig_](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.backend_config.BackendConfig.html#torch.ao.quantization.backend_config.BackendConfig "torch.ao.quantization.backend_config.backend_config.BackendConfig")

torch.ao.quantization.backend\_config.utils[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#torch-ao-quantization-backend-config-utils "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`entry_to_pretty_str`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.backend_config.utils.entry_to_pretty_str.html#torch.ao.quantization.backend_config.utils.entry_to_pretty_str "torch.ao.quantization.backend_config.utils.entry_to_pretty_str") | Given a backend\_config\_dict entry, returns a string with the human readable representation of it. |
| [`get_fused_module_classes`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.backend_config.utils.get_fused_module_classes.html#torch.ao.quantization.backend_config.utils.get_fused_module_classes "torch.ao.quantization.backend_config.utils.get_fused_module_classes") |     |
| [`get_fuser_method_mapping`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.backend_config.utils.get_fuser_method_mapping.html#torch.ao.quantization.backend_config.utils.get_fuser_method_mapping "torch.ao.quantization.backend_config.utils.get_fuser_method_mapping") |     |
| [`get_fusion_pattern_to_extra_inputs_getter`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.backend_config.utils.get_fusion_pattern_to_extra_inputs_getter.html#torch.ao.quantization.backend_config.utils.get_fusion_pattern_to_extra_inputs_getter "torch.ao.quantization.backend_config.utils.get_fusion_pattern_to_extra_inputs_getter") | Get a map from fusion pattern to a function that returns extra input nodes from the fusion pattern, in the order required by the root node. |
| [`get_fusion_pattern_to_root_node_getter`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.backend_config.utils.get_fusion_pattern_to_root_node_getter.html#torch.ao.quantization.backend_config.utils.get_fusion_pattern_to_root_node_getter "torch.ao.quantization.backend_config.utils.get_fusion_pattern_to_root_node_getter") | Get a map from fusion pattern to a function that returns the root node from the fusion pattern, e.g. the most common one is::. |
| [`get_module_to_qat_module`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.backend_config.utils.get_module_to_qat_module.html#torch.ao.quantization.backend_config.utils.get_module_to_qat_module "torch.ao.quantization.backend_config.utils.get_module_to_qat_module") |     |
| [`get_pattern_to_dtype_configs`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.backend_config.utils.get_pattern_to_dtype_configs.html#torch.ao.quantization.backend_config.utils.get_pattern_to_dtype_configs "torch.ao.quantization.backend_config.utils.get_pattern_to_dtype_configs") |     |
| [`get_pattern_to_input_type_to_index`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.backend_config.utils.get_pattern_to_input_type_to_index.html#torch.ao.quantization.backend_config.utils.get_pattern_to_input_type_to_index "torch.ao.quantization.backend_config.utils.get_pattern_to_input_type_to_index") |     |
| [`get_qat_module_classes`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.backend_config.utils.get_qat_module_classes.html#torch.ao.quantization.backend_config.utils.get_qat_module_classes "torch.ao.quantization.backend_config.utils.get_qat_module_classes") |     |
| [`get_root_module_to_quantized_reference_module`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.backend_config.utils.get_root_module_to_quantized_reference_module.html#torch.ao.quantization.backend_config.utils.get_root_module_to_quantized_reference_module "torch.ao.quantization.backend_config.utils.get_root_module_to_quantized_reference_module") |     |
| [`pattern_to_human_readable`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.backend_config.utils.pattern_to_human_readable.html#torch.ao.quantization.backend_config.utils.pattern_to_human_readable "torch.ao.quantization.backend_config.utils.pattern_to_human_readable") |     |
| [`remove_boolean_dispatch_from_name`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.backend_config.utils.remove_boolean_dispatch_from_name.html#torch.ao.quantization.backend_config.utils.remove_boolean_dispatch_from_name "torch.ao.quantization.backend_config.utils.remove_boolean_dispatch_from_name") | Some ops have a default string representation such as '<function boolean\_dispatch.<locals>.fn at 0x7ff1106bf280>', this function replaces them with the hardcoded function names. |

torch.ao.quantization.fx.custom\_config[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#torch-ao-quantization-fx-custom-config "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

This module contains a few CustomConfig classes that’s used in both eager mode and FX graph mode quantization

|     |     |
| --- | --- |
| [`FuseCustomConfig`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fx.custom_config.FuseCustomConfig.html#torch.ao.quantization.fx.custom_config.FuseCustomConfig "torch.ao.quantization.fx.custom_config.FuseCustomConfig") | Custom configuration for [`fuse_fx()`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantize_fx.fuse_fx.html#torch.ao.quantization.quantize_fx.fuse_fx "torch.ao.quantization.quantize_fx.fuse_fx")<br>. |
| [`PrepareCustomConfig`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fx.custom_config.PrepareCustomConfig.html#torch.ao.quantization.fx.custom_config.PrepareCustomConfig "torch.ao.quantization.fx.custom_config.PrepareCustomConfig") | Custom configuration for [`prepare_fx()`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantize_fx.prepare_fx.html#torch.ao.quantization.quantize_fx.prepare_fx "torch.ao.quantization.quantize_fx.prepare_fx")<br> and [`prepare_qat_fx()`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantize_fx.prepare_qat_fx.html#torch.ao.quantization.quantize_fx.prepare_qat_fx "torch.ao.quantization.quantize_fx.prepare_qat_fx")<br>. |
| [`ConvertCustomConfig`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fx.custom_config.ConvertCustomConfig.html#torch.ao.quantization.fx.custom_config.ConvertCustomConfig "torch.ao.quantization.fx.custom_config.ConvertCustomConfig") | Custom configuration for [`convert_fx()`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantize_fx.convert_fx.html#torch.ao.quantization.quantize_fx.convert_fx "torch.ao.quantization.quantize_fx.convert_fx")<br>. |
| [`StandaloneModuleConfigEntry`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fx.custom_config.StandaloneModuleConfigEntry.html#torch.ao.quantization.fx.custom_config.StandaloneModuleConfigEntry "torch.ao.quantization.fx.custom_config.StandaloneModuleConfigEntry") |     |

torch.ao.quantization.fx.graph\_module[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#torch-ao-quantization-fx-graph-module "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`QuantizedGraphModule`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fx.graph_module.QuantizedGraphModule.html#torch.ao.quantization.fx.graph_module.QuantizedGraphModule "torch.ao.quantization.fx.graph_module.QuantizedGraphModule") | This class is created to make sure PackedParams (e.g. LinearPackedParams, Conv2dPackedParams) to appear in state\_dict so that we can serialize and deserialize quantized graph module with torch.save(m.state\_dict()) and m.load\_state\_dict(state\_dict). |

torch.ao.quantization.fx.utils[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#torch-ao-quantization-fx-utils "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`all_node_args_except_first`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fx.utils.all_node_args_except_first.html#torch.ao.quantization.fx.utils.all_node_args_except_first "torch.ao.quantization.fx.utils.all_node_args_except_first") | Returns all node arg indices after first |
| [`all_node_args_have_no_tensors`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fx.utils.all_node_args_have_no_tensors.html#torch.ao.quantization.fx.utils.all_node_args_have_no_tensors "torch.ao.quantization.fx.utils.all_node_args_have_no_tensors") | If we know for sure that all of this node's args have no tensors (are primitives), return True. |
| [`assert_and_get_unique_device`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fx.utils.assert_and_get_unique_device.html#torch.ao.quantization.fx.utils.assert_and_get_unique_device "torch.ao.quantization.fx.utils.assert_and_get_unique_device") | Returns the unique device for a module, or None if no device is found. |
| [`collect_producer_nodes`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fx.utils.collect_producer_nodes.html#torch.ao.quantization.fx.utils.collect_producer_nodes "torch.ao.quantization.fx.utils.collect_producer_nodes") | Starting from a target node, trace back until we hit input or getattr node. This is used to extract the chain of operators starting from getattr to the target node, for example::. |
| [`create_getattr_from_value`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fx.utils.create_getattr_from_value.html#torch.ao.quantization.fx.utils.create_getattr_from_value "torch.ao.quantization.fx.utils.create_getattr_from_value") | Given a value of any type, creates a getattr node corresponding to the value and registers the value as a buffer to the module. |
| [`create_node_from_old_node_preserve_meta`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fx.utils.create_node_from_old_node_preserve_meta.html#torch.ao.quantization.fx.utils.create_node_from_old_node_preserve_meta "torch.ao.quantization.fx.utils.create_node_from_old_node_preserve_meta") | Creates new\_node and copies the necessary metadata to it from old\_node. |
| [`get_custom_module_class_keys`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fx.utils.get_custom_module_class_keys.html#torch.ao.quantization.fx.utils.get_custom_module_class_keys "torch.ao.quantization.fx.utils.get_custom_module_class_keys") | Get all the unique custom module keys in the custom config dict. |
| [`get_linear_prepack_op_for_dtype`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fx.utils.get_linear_prepack_op_for_dtype.html#torch.ao.quantization.fx.utils.get_linear_prepack_op_for_dtype "torch.ao.quantization.fx.utils.get_linear_prepack_op_for_dtype") |     |
| [`get_new_attr_name_with_prefix`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fx.utils.get_new_attr_name_with_prefix.html#torch.ao.quantization.fx.utils.get_new_attr_name_with_prefix "torch.ao.quantization.fx.utils.get_new_attr_name_with_prefix") |     |
| [`get_non_observable_arg_indexes_and_types`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fx.utils.get_non_observable_arg_indexes_and_types.html#torch.ao.quantization.fx.utils.get_non_observable_arg_indexes_and_types "torch.ao.quantization.fx.utils.get_non_observable_arg_indexes_and_types") | Returns a dict with of non float tensor types as keys and values which correspond to a function to retrieve the list (which takes the node as an argument) |
| [`get_qconv_prepack_op`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fx.utils.get_qconv_prepack_op.html#torch.ao.quantization.fx.utils.get_qconv_prepack_op "torch.ao.quantization.fx.utils.get_qconv_prepack_op") |     |
| [`get_skipped_module_name_and_classes`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fx.utils.get_skipped_module_name_and_classes.html#torch.ao.quantization.fx.utils.get_skipped_module_name_and_classes "torch.ao.quantization.fx.utils.get_skipped_module_name_and_classes") |     |
| [`graph_module_from_producer_nodes`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fx.utils.graph_module_from_producer_nodes.html#torch.ao.quantization.fx.utils.graph_module_from_producer_nodes "torch.ao.quantization.fx.utils.graph_module_from_producer_nodes") | Construct a graph module from extracted producer nodes from collect\_producer\_nodes function :param root: the root module for the original graph :param producer\_nodes: a list of nodes we use to construct the graph |
| [`maybe_get_next_module`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fx.utils.maybe_get_next_module.html#torch.ao.quantization.fx.utils.maybe_get_next_module "torch.ao.quantization.fx.utils.maybe_get_next_module") | Gets the next module that matches what is needed in is\_target\_module\_type if it exists |
| [`node_arg_is_bias`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fx.utils.node_arg_is_bias.html#torch.ao.quantization.fx.utils.node_arg_is_bias "torch.ao.quantization.fx.utils.node_arg_is_bias") | Returns if node arg is bias |
| [`node_arg_is_weight`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fx.utils.node_arg_is_weight.html#torch.ao.quantization.fx.utils.node_arg_is_weight "torch.ao.quantization.fx.utils.node_arg_is_weight") | Returns if node arg is weight |
| [`NodeInfo`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fx.utils.NodeInfo.html#torch.ao.quantization.fx.utils.NodeInfo "torch.ao.quantization.fx.utils.NodeInfo") |     |
| [`return_arg_list`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fx.utils.return_arg_list.html#torch.ao.quantization.fx.utils.return_arg_list "torch.ao.quantization.fx.utils.return_arg_list") | Constructs a function that takes a node as arg and returns the arg\_indices that are valid for node.args |

torch (quantization related functions)[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#torch-quantization-related-functions "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

This describes the quantization related functions of the `torch` namespace.

|     |     |
| --- | --- |
| [`quantize_per_tensor`](https://docs.pytorch.org/docs/2.15/generated/torch.quantize_per_tensor.html#torch.quantize_per_tensor "torch.quantize_per_tensor") | Converts a float tensor to a quantized tensor with given scale and zero point. |
| [`quantize_per_channel`](https://docs.pytorch.org/docs/2.15/generated/torch.quantize_per_channel.html#torch.quantize_per_channel "torch.quantize_per_channel") | Converts a float tensor to a per-channel quantized tensor with given scales and zero points. |
| [`dequantize`](https://docs.pytorch.org/docs/2.15/generated/torch.dequantize.html#torch.dequantize "torch.dequantize") | Returns an fp32 Tensor by dequantizing a quantized Tensor |

torch.Tensor (quantization related methods)[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#torch-tensor-quantization-related-methods "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Quantized Tensors support a limited subset of data manipulation methods of the regular full-precision tensor.

|     |     |
| --- | --- |
| [`view`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.view.html#torch.Tensor.view "torch.Tensor.view") | Returns a new tensor with the same data as the `self` tensor but of a different [`shape`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.shape.html#torch.Tensor.shape "torch.Tensor.shape")<br>. |
| [`as_strided`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.as_strided.html#torch.Tensor.as_strided "torch.Tensor.as_strided") | See [`torch.as_strided()`](https://docs.pytorch.org/docs/2.15/generated/torch.as_strided.html#torch.as_strided "torch.as_strided") |
| [`expand`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.expand.html#torch.Tensor.expand "torch.Tensor.expand") | Returns a new view of the `self` tensor with singleton dimensions expanded to a larger size. |
| [`flatten`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.flatten.html#torch.Tensor.flatten "torch.Tensor.flatten") | See [`torch.flatten()`](https://docs.pytorch.org/docs/2.15/generated/torch.flatten.html#torch.flatten "torch.flatten") |
| [`select`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.select.html#torch.Tensor.select "torch.Tensor.select") | See [`torch.select()`](https://docs.pytorch.org/docs/2.15/generated/torch.select.html#torch.select "torch.select") |
| [`ne`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.ne.html#torch.Tensor.ne "torch.Tensor.ne") | See [`torch.ne()`](https://docs.pytorch.org/docs/2.15/generated/torch.ne.html#torch.ne "torch.ne")<br>. |
| [`eq`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.eq.html#torch.Tensor.eq "torch.Tensor.eq") | See [`torch.eq()`](https://docs.pytorch.org/docs/2.15/generated/torch.eq.html#torch.eq "torch.eq") |
| [`ge`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.ge.html#torch.Tensor.ge "torch.Tensor.ge") | See [`torch.ge()`](https://docs.pytorch.org/docs/2.15/generated/torch.ge.html#torch.ge "torch.ge")<br>. |
| [`le`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.le.html#torch.Tensor.le "torch.Tensor.le") | See [`torch.le()`](https://docs.pytorch.org/docs/2.15/generated/torch.le.html#torch.le "torch.le")<br>. |
| [`gt`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.gt.html#torch.Tensor.gt "torch.Tensor.gt") | See [`torch.gt()`](https://docs.pytorch.org/docs/2.15/generated/torch.gt.html#torch.gt "torch.gt")<br>. |
| [`lt`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.lt.html#torch.Tensor.lt "torch.Tensor.lt") | See [`torch.lt()`](https://docs.pytorch.org/docs/2.15/generated/torch.lt.html#torch.lt "torch.lt")<br>. |
| [`copy_`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.copy_.html#torch.Tensor.copy_ "torch.Tensor.copy_") | Copies the elements from `src` into `self` tensor and returns `self`. |
| [`clone`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.clone.html#torch.Tensor.clone "torch.Tensor.clone") | See [`torch.clone()`](https://docs.pytorch.org/docs/2.15/generated/torch.clone.html#torch.clone "torch.clone") |
| [`dequantize`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.dequantize.html#torch.Tensor.dequantize "torch.Tensor.dequantize") | Given a quantized Tensor, dequantize it and return the dequantized float Tensor. |
| [`equal`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.equal.html#torch.Tensor.equal "torch.Tensor.equal") | See [`torch.equal()`](https://docs.pytorch.org/docs/2.15/generated/torch.equal.html#torch.equal "torch.equal") |
| [`int_repr`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.int_repr.html#torch.Tensor.int_repr "torch.Tensor.int_repr") | Given a quantized Tensor, `self.int_repr()` returns a CPU Tensor with uint8\_t as data type that stores the underlying uint8\_t values of the given Tensor. |
| [`max`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.max.html#torch.Tensor.max "torch.Tensor.max") | See [`torch.max()`](https://docs.pytorch.org/docs/2.15/generated/torch.max.html#torch.max "torch.max") |
| [`mean`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.mean.html#torch.Tensor.mean "torch.Tensor.mean") | See [`torch.mean()`](https://docs.pytorch.org/docs/2.15/generated/torch.mean.html#torch.mean "torch.mean") |
| [`min`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.min.html#torch.Tensor.min "torch.Tensor.min") | See [`torch.min()`](https://docs.pytorch.org/docs/2.15/generated/torch.min.html#torch.min "torch.min") |
| [`q_scale`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.q_scale.html#torch.Tensor.q_scale "torch.Tensor.q_scale") | Given a Tensor quantized by linear(affine) quantization, returns the scale of the underlying quantizer(). |
| [`q_zero_point`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.q_zero_point.html#torch.Tensor.q_zero_point "torch.Tensor.q_zero_point") | Given a Tensor quantized by linear(affine) quantization, returns the zero\_point of the underlying quantizer(). |
| [`q_per_channel_scales`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.q_per_channel_scales.html#torch.Tensor.q_per_channel_scales "torch.Tensor.q_per_channel_scales") | Given a Tensor quantized by linear (affine) per-channel quantization, returns a Tensor of scales of the underlying quantizer. |
| [`q_per_channel_zero_points`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.q_per_channel_zero_points.html#torch.Tensor.q_per_channel_zero_points "torch.Tensor.q_per_channel_zero_points") | Given a Tensor quantized by linear (affine) per-channel quantization, returns a tensor of zero\_points of the underlying quantizer. |
| [`q_per_channel_axis`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.q_per_channel_axis.html#torch.Tensor.q_per_channel_axis "torch.Tensor.q_per_channel_axis") | Given a Tensor quantized by linear (affine) per-channel quantization, returns the index of dimension on which per-channel quantization is applied. |
| [`resize_`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.resize_.html#torch.Tensor.resize_ "torch.Tensor.resize_") | Resizes `self` tensor to the specified size. |
| [`sort`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.sort.html#torch.Tensor.sort "torch.Tensor.sort") | See [`torch.sort()`](https://docs.pytorch.org/docs/2.15/generated/torch.sort.html#torch.sort "torch.sort") |
| [`topk`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.topk.html#torch.Tensor.topk "torch.Tensor.topk") | See [`torch.topk()`](https://docs.pytorch.org/docs/2.15/generated/torch.topk.html#torch.topk "torch.topk") |

torch.ao.quantization.observer[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#torch-ao-quantization-observer "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

This module contains observers which are used to collect statistics about the values observed during calibration (PTQ) or training (QAT).

|     |     |
| --- | --- |
| [`ObserverBase`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.ObserverBase.html#torch.ao.quantization.observer.ObserverBase "torch.ao.quantization.observer.ObserverBase") | Base observer Module. |
| [`MinMaxObserver`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.MinMaxObserver.html#torch.ao.quantization.observer.MinMaxObserver "torch.ao.quantization.observer.MinMaxObserver") | Observer module for computing the quantization parameters based on the running min and max values. |
| [`MovingAverageMinMaxObserver`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.MovingAverageMinMaxObserver.html#torch.ao.quantization.observer.MovingAverageMinMaxObserver "torch.ao.quantization.observer.MovingAverageMinMaxObserver") | Observer module for computing the quantization parameters based on the moving average of the min and max values. |
| [`PerChannelMinMaxObserver`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.PerChannelMinMaxObserver.html#torch.ao.quantization.observer.PerChannelMinMaxObserver "torch.ao.quantization.observer.PerChannelMinMaxObserver") | Observer module for computing the quantization parameters based on the running per channel min and max values. |
| [`MovingAveragePerChannelMinMaxObserver`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.MovingAveragePerChannelMinMaxObserver.html#torch.ao.quantization.observer.MovingAveragePerChannelMinMaxObserver "torch.ao.quantization.observer.MovingAveragePerChannelMinMaxObserver") | Observer module for computing the quantization parameters based on the running per channel min and max values. |
| [`HistogramObserver`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.HistogramObserver.html#torch.ao.quantization.observer.HistogramObserver "torch.ao.quantization.observer.HistogramObserver") | The module records the running histogram of tensor values along with min/max values. |
| [`PlaceholderObserver`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.PlaceholderObserver.html#torch.ao.quantization.observer.PlaceholderObserver "torch.ao.quantization.observer.PlaceholderObserver") | Observer that doesn't do anything and just passes its configuration to the quantized module's `.from_float()`. |
| [`RecordingObserver`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.RecordingObserver.html#torch.ao.quantization.observer.RecordingObserver "torch.ao.quantization.observer.RecordingObserver") | The module is mainly for debug and records the tensor values during runtime. |
| [`NoopObserver`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.NoopObserver.html#torch.ao.quantization.observer.NoopObserver "torch.ao.quantization.observer.NoopObserver") | Observer that doesn't do anything and just passes its configuration to the quantized module's `.from_float()`. |
| [`get_observer_state_dict`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.get_observer_state_dict.html#torch.ao.quantization.observer.get_observer_state_dict "torch.ao.quantization.observer.get_observer_state_dict") | Returns the state dict corresponding to the observer stats. |
| [`load_observer_state_dict`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.load_observer_state_dict.html#torch.ao.quantization.observer.load_observer_state_dict "torch.ao.quantization.observer.load_observer_state_dict") | Given input model and a state\_dict containing model observer stats, load the stats back into the model. |
| [`default_affine_fixed_qparams_observer`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.default_affine_fixed_qparams_observer.html#torch.ao.quantization.observer.default_affine_fixed_qparams_observer "torch.ao.quantization.observer.default_affine_fixed_qparams_observer") | Default observers for fixed qparams operations. |
| [`default_observer`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.default_observer.html#torch.ao.quantization.observer.default_observer "torch.ao.quantization.observer.default_observer") | Default observer for static quantization, usually used for debugging. |
| [`default_placeholder_observer`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.default_placeholder_observer.html#torch.ao.quantization.observer.default_placeholder_observer "torch.ao.quantization.observer.default_placeholder_observer") | Default placeholder observer, usually used for quantization to torch.float16. |
| [`default_debug_observer`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.default_debug_observer.html#torch.ao.quantization.observer.default_debug_observer "torch.ao.quantization.observer.default_debug_observer") | Default debug-only observer. |
| [`default_weight_observer`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.default_weight_observer.html#torch.ao.quantization.observer.default_weight_observer "torch.ao.quantization.observer.default_weight_observer") | Default weight observer. |
| [`default_histogram_observer`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.default_histogram_observer.html#torch.ao.quantization.observer.default_histogram_observer "torch.ao.quantization.observer.default_histogram_observer") | Default histogram observer, usually used for PTQ. |
| [`default_per_channel_weight_observer`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.default_per_channel_weight_observer.html#torch.ao.quantization.observer.default_per_channel_weight_observer "torch.ao.quantization.observer.default_per_channel_weight_observer") | Default per-channel weight observer, usually used on backends where per-channel weight quantization is supported, such as fbgemm. |
| [`default_dynamic_quant_observer`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.default_dynamic_quant_observer.html#torch.ao.quantization.observer.default_dynamic_quant_observer "torch.ao.quantization.observer.default_dynamic_quant_observer") | Default observer for dynamic quantization. |
| [`default_fixed_qparams_range_0to1_observer`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.default_fixed_qparams_range_0to1_observer.html#torch.ao.quantization.observer.default_fixed_qparams_range_0to1_observer "torch.ao.quantization.observer.default_fixed_qparams_range_0to1_observer") |     |
| [`default_fixed_qparams_range_neg1to1_observer`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.default_fixed_qparams_range_neg1to1_observer.html#torch.ao.quantization.observer.default_fixed_qparams_range_neg1to1_observer "torch.ao.quantization.observer.default_fixed_qparams_range_neg1to1_observer") |     |
| [`default_float_qparams_observer`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.default_float_qparams_observer.html#torch.ao.quantization.observer.default_float_qparams_observer "torch.ao.quantization.observer.default_float_qparams_observer") | Default observer for a floating point zero-point. |
| [`default_float_qparams_observer_4bit`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.default_float_qparams_observer_4bit.html#torch.ao.quantization.observer.default_float_qparams_observer_4bit "torch.ao.quantization.observer.default_float_qparams_observer_4bit") | Default observer for a floating point zero-point and 4 bit activations. |
| [`default_symmetric_fixed_qparams_observer`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.default_symmetric_fixed_qparams_observer.html#torch.ao.quantization.observer.default_symmetric_fixed_qparams_observer "torch.ao.quantization.observer.default_symmetric_fixed_qparams_observer") |     |
| [`per_channel_weight_observer_range_neg_127_to_127`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.per_channel_weight_observer_range_neg_127_to_127.html#torch.ao.quantization.observer.per_channel_weight_observer_range_neg_127_to_127 "torch.ao.quantization.observer.per_channel_weight_observer_range_neg_127_to_127") | Per-channel, symmetric weight observer with the 8-bit values restricted to \[-127, +127\], excluding -128. |
| [`weight_observer_range_neg_127_to_127`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.weight_observer_range_neg_127_to_127.html#torch.ao.quantization.observer.weight_observer_range_neg_127_to_127 "torch.ao.quantization.observer.weight_observer_range_neg_127_to_127") | Symmetric weight observer with the 8-bit values restricted to \[-127, +127\], excluding -128. |
| [`AffineQuantizedObserverBase`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.AffineQuantizedObserverBase.html#torch.ao.quantization.observer.AffineQuantizedObserverBase "torch.ao.quantization.observer.AffineQuantizedObserverBase") | Observer module for affine quantization ([pytorch/ao](https://github.com/pytorch/ao/tree/main/torchao/quantization#affine-quantization)<br>) |
| [`Granularity`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.Granularity.html#torch.ao.quantization.observer.Granularity "torch.ao.quantization.observer.Granularity") | Base class for representing the granularity of quantization. |
| [`MappingType`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.MappingType.html#torch.ao.quantization.observer.MappingType "torch.ao.quantization.observer.MappingType") | How floating point number is mapped to integer number |
| [`PerAxis`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.PerAxis.html#torch.ao.quantization.observer.PerAxis "torch.ao.quantization.observer.PerAxis") | Represents per-axis granularity in quantization. |
| [`PerBlock`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.PerBlock.html#torch.ao.quantization.observer.PerBlock "torch.ao.quantization.observer.PerBlock") | Represents per-block granularity in quantization. |
| [`PerGroup`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.PerGroup.html#torch.ao.quantization.observer.PerGroup "torch.ao.quantization.observer.PerGroup") | Represents per-channel group granularity in quantization. |
| [`PerRow`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.PerRow.html#torch.ao.quantization.observer.PerRow "torch.ao.quantization.observer.PerRow") | Represents row-wise granularity in quantization. |
| [`PerTensor`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.PerTensor.html#torch.ao.quantization.observer.PerTensor "torch.ao.quantization.observer.PerTensor") | Represents per-tensor granularity in quantization. |
| [`PerToken`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.PerToken.html#torch.ao.quantization.observer.PerToken "torch.ao.quantization.observer.PerToken") | Represents per-token granularity in quantization. |
| [`TorchAODType`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.TorchAODType.html#torch.ao.quantization.observer.TorchAODType "torch.ao.quantization.observer.TorchAODType") | Placeholder for dtypes that do not exist in PyTorch core yet. |
| [`ZeroPointDomain`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.ZeroPointDomain.html#torch.ao.quantization.observer.ZeroPointDomain "torch.ao.quantization.observer.ZeroPointDomain") | Enum that indicate whether zero\_point is in integer domain or floating point domain |
| [`get_block_size`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.get_block_size.html#torch.ao.quantization.observer.get_block_size "torch.ao.quantization.observer.get_block_size") | Get the block size based on the input shape and granularity type. |

torch.ao.quantization.fake\_quantize[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#torch-ao-quantization-fake-quantize "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

This module implements modules which are used to perform fake quantization during QAT.

|     |     |
| --- | --- |
| [`FakeQuantizeBase`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fake_quantize.FakeQuantizeBase.html#torch.ao.quantization.fake_quantize.FakeQuantizeBase "torch.ao.quantization.fake_quantize.FakeQuantizeBase") | Base fake quantize module. |
| [`FakeQuantize`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fake_quantize.FakeQuantize.html#torch.ao.quantization.fake_quantize.FakeQuantize "torch.ao.quantization.fake_quantize.FakeQuantize") | Simulate the quantize and dequantize operations in training time. |
| [`FixedQParamsFakeQuantize`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fake_quantize.FixedQParamsFakeQuantize.html#torch.ao.quantization.fake_quantize.FixedQParamsFakeQuantize "torch.ao.quantization.fake_quantize.FixedQParamsFakeQuantize") | Simulate quantize and dequantize in training time. |
| [`FusedMovingAvgObsFakeQuantize`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fake_quantize.FusedMovingAvgObsFakeQuantize.html#torch.ao.quantization.fake_quantize.FusedMovingAvgObsFakeQuantize "torch.ao.quantization.fake_quantize.FusedMovingAvgObsFakeQuantize") | Define a fused module to observe the tensor. |
| [`default_affine_fixed_qparams_fake_quant`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fake_quantize.default_affine_fixed_qparams_fake_quant.html#torch.ao.quantization.fake_quantize.default_affine_fixed_qparams_fake_quant "torch.ao.quantization.fake_quantize.default_affine_fixed_qparams_fake_quant") |     |
| [`default_dynamic_fake_quant`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fake_quantize.default_dynamic_fake_quant.html#torch.ao.quantization.fake_quantize.default_dynamic_fake_quant "torch.ao.quantization.fake_quantize.default_dynamic_fake_quant") | Default dynamic fake\_quant for activations. |
| [`default_embedding_fake_quant`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fake_quantize.default_embedding_fake_quant.html#torch.ao.quantization.fake_quantize.default_embedding_fake_quant "torch.ao.quantization.fake_quantize.default_embedding_fake_quant") | Default fake\_quant for embeddings. |
| [`default_embedding_fake_quant_4bit`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fake_quantize.default_embedding_fake_quant_4bit.html#torch.ao.quantization.fake_quantize.default_embedding_fake_quant_4bit "torch.ao.quantization.fake_quantize.default_embedding_fake_quant_4bit") |     |
| [`default_fake_quant`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fake_quantize.default_fake_quant.html#torch.ao.quantization.fake_quantize.default_fake_quant "torch.ao.quantization.fake_quantize.default_fake_quant") | Default fake\_quant for activations. |
| [`default_fixed_qparams_range_0to1_fake_quant`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fake_quantize.default_fixed_qparams_range_0to1_fake_quant.html#torch.ao.quantization.fake_quantize.default_fixed_qparams_range_0to1_fake_quant "torch.ao.quantization.fake_quantize.default_fixed_qparams_range_0to1_fake_quant") |     |
| [`default_fixed_qparams_range_neg1to1_fake_quant`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fake_quantize.default_fixed_qparams_range_neg1to1_fake_quant.html#torch.ao.quantization.fake_quantize.default_fixed_qparams_range_neg1to1_fake_quant "torch.ao.quantization.fake_quantize.default_fixed_qparams_range_neg1to1_fake_quant") |     |
| [`default_fused_act_fake_quant`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fake_quantize.default_fused_act_fake_quant.html#torch.ao.quantization.fake_quantize.default_fused_act_fake_quant "torch.ao.quantization.fake_quantize.default_fused_act_fake_quant") | Fused version of default\_fake\_quant, with improved performance. |
| [`default_fused_per_channel_wt_fake_quant`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fake_quantize.default_fused_per_channel_wt_fake_quant.html#torch.ao.quantization.fake_quantize.default_fused_per_channel_wt_fake_quant "torch.ao.quantization.fake_quantize.default_fused_per_channel_wt_fake_quant") | Fused version of default\_per\_channel\_weight\_fake\_quant, with improved performance. |
| [`default_fused_wt_fake_quant`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fake_quantize.default_fused_wt_fake_quant.html#torch.ao.quantization.fake_quantize.default_fused_wt_fake_quant "torch.ao.quantization.fake_quantize.default_fused_wt_fake_quant") | Fused version of default\_weight\_fake\_quant, with improved performance. |
| [`default_histogram_fake_quant`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fake_quantize.default_histogram_fake_quant.html#torch.ao.quantization.fake_quantize.default_histogram_fake_quant "torch.ao.quantization.fake_quantize.default_histogram_fake_quant") | Fake\_quant for activations using a histogram.. |
| [`default_per_channel_weight_fake_quant`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fake_quantize.default_per_channel_weight_fake_quant.html#torch.ao.quantization.fake_quantize.default_per_channel_weight_fake_quant "torch.ao.quantization.fake_quantize.default_per_channel_weight_fake_quant") | Default fake\_quant for per-channel weights. |
| [`default_symmetric_fixed_qparams_fake_quant`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fake_quantize.default_symmetric_fixed_qparams_fake_quant.html#torch.ao.quantization.fake_quantize.default_symmetric_fixed_qparams_fake_quant "torch.ao.quantization.fake_quantize.default_symmetric_fixed_qparams_fake_quant") |     |
| [`default_weight_fake_quant`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fake_quantize.default_weight_fake_quant.html#torch.ao.quantization.fake_quantize.default_weight_fake_quant "torch.ao.quantization.fake_quantize.default_weight_fake_quant") | Default fake\_quant for weights. |
| [`disable_fake_quant`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fake_quantize.disable_fake_quant.html#torch.ao.quantization.fake_quantize.disable_fake_quant "torch.ao.quantization.fake_quantize.disable_fake_quant") | Disable fake quantization for the module. |
| [`disable_observer`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fake_quantize.disable_observer.html#torch.ao.quantization.fake_quantize.disable_observer "torch.ao.quantization.fake_quantize.disable_observer") | Disable observation for this module. |
| [`enable_fake_quant`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fake_quantize.enable_fake_quant.html#torch.ao.quantization.fake_quantize.enable_fake_quant "torch.ao.quantization.fake_quantize.enable_fake_quant") | Enable fake quantization for the module. |
| [`enable_observer`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fake_quantize.enable_observer.html#torch.ao.quantization.fake_quantize.enable_observer "torch.ao.quantization.fake_quantize.enable_observer") | Enable observation for this module. |
| [`fused_per_channel_wt_fake_quant_range_neg_127_to_127`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fake_quantize.fused_per_channel_wt_fake_quant_range_neg_127_to_127.html#torch.ao.quantization.fake_quantize.fused_per_channel_wt_fake_quant_range_neg_127_to_127 "torch.ao.quantization.fake_quantize.fused_per_channel_wt_fake_quant_range_neg_127_to_127") | Fused version of default\_per\_channel\_weight\_fake\_quant, with the 8-bit values restricted to \[-127, +127\], excluding -128. |
| [`fused_wt_fake_quant_range_neg_127_to_127`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.fake_quantize.fused_wt_fake_quant_range_neg_127_to_127.html#torch.ao.quantization.fake_quantize.fused_wt_fake_quant_range_neg_127_to_127 "torch.ao.quantization.fake_quantize.fused_wt_fake_quant_range_neg_127_to_127") | Fused version of default\_weight\_fake\_quant, with the 8-bit values restricted to \[-127, +127\], excluding -128. |

torch.ao.quantization.qconfig[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#torch-ao-quantization-qconfig "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

This module defines `QConfig` objects which are used to configure quantization settings for individual ops.

torch.ao.quantization.qconfig.get\_default\_qat\_qconfig(_backend\='x86'_, _version\=1_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/ao/quantization/qconfig.py#L374)
[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#torch.ao.quantization.qconfig.get_default_qat_qconfig "Link to this definition")

Returns the default QAT qconfig for the specified backend.

Parameters:

*   **backend** (_\*_) – a string representing the target backend. Currently supports x86 (default), fbgemm, qnnpack and onednn.
    
*   **version** (_\*_) – version, for backwards compatibility. Can be None or 1.
    

Returns:

qconfig

torch.ao.quantization.qconfig.get\_default\_qconfig(_backend\='x86'_, _version\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/ao/quantization/qconfig.py#L259)
[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#torch.ao.quantization.qconfig.get_default_qconfig "Link to this definition")

Returns the default PTQ qconfig for the specified backend.

Parameters:

**backend** (_\*_) – a string representing the target backend. Currently supports x86 (default), fbgemm, qnnpack and onednn.

Returns:

qconfig

torch.ao.quantization.qconfig.qconfig\_equals(_q1_, _q2_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/ao/quantization/qconfig.py#L663)
[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#torch.ao.quantization.qconfig.qconfig_equals "Link to this definition")

Returns True if q1 equals q2, and False otherwise.

|     |     |
| --- | --- |
| [`QConfig`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.qconfig.QConfig.html#torch.ao.quantization.qconfig.QConfig "torch.ao.quantization.qconfig.QConfig") | Describes how to quantize a layer or a part of the network by providing settings (observer classes) for activations and weights respectively. |
| [`QConfigAny`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.qconfig.QConfigAny.html#torch.ao.quantization.qconfig.QConfigAny "torch.ao.quantization.qconfig.QConfigAny") | Create named, parameterized type aliases. |
| [`default_qconfig`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.qconfig.default_qconfig.html#torch.ao.quantization.qconfig.default_qconfig "torch.ao.quantization.qconfig.default_qconfig") | Default qconfig configuration. |
| [`default_debug_qconfig`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.qconfig.default_debug_qconfig.html#torch.ao.quantization.qconfig.default_debug_qconfig "torch.ao.quantization.qconfig.default_debug_qconfig") | Default qconfig configuration for debugging. |
| [`default_per_channel_qconfig`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.qconfig.default_per_channel_qconfig.html#torch.ao.quantization.qconfig.default_per_channel_qconfig "torch.ao.quantization.qconfig.default_per_channel_qconfig") | Default qconfig configuration for per channel weight quantization. |
| [`default_dynamic_qconfig`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.qconfig.default_dynamic_qconfig.html#torch.ao.quantization.qconfig.default_dynamic_qconfig "torch.ao.quantization.qconfig.default_dynamic_qconfig") | Default dynamic qconfig. |
| [`float16_dynamic_qconfig`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.qconfig.float16_dynamic_qconfig.html#torch.ao.quantization.qconfig.float16_dynamic_qconfig "torch.ao.quantization.qconfig.float16_dynamic_qconfig") | Dynamic qconfig with weights quantized to torch.float16. |
| [`float16_static_qconfig`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.qconfig.float16_static_qconfig.html#torch.ao.quantization.qconfig.float16_static_qconfig "torch.ao.quantization.qconfig.float16_static_qconfig") | Dynamic qconfig with both activations and weights quantized to torch.float16. |
| [`per_channel_dynamic_qconfig`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.qconfig.per_channel_dynamic_qconfig.html#torch.ao.quantization.qconfig.per_channel_dynamic_qconfig "torch.ao.quantization.qconfig.per_channel_dynamic_qconfig") | Dynamic qconfig with weights quantized per channel. |
| [`float_qparams_weight_only_qconfig`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.qconfig.float_qparams_weight_only_qconfig.html#torch.ao.quantization.qconfig.float_qparams_weight_only_qconfig "torch.ao.quantization.qconfig.float_qparams_weight_only_qconfig") | Dynamic qconfig with weights quantized with a floating point zero\_point. |
| [`default_qat_qconfig`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.qconfig.default_qat_qconfig.html#torch.ao.quantization.qconfig.default_qat_qconfig "torch.ao.quantization.qconfig.default_qat_qconfig") | Default qconfig for QAT. |
| [`default_weight_only_qconfig`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.qconfig.default_weight_only_qconfig.html#torch.ao.quantization.qconfig.default_weight_only_qconfig "torch.ao.quantization.qconfig.default_weight_only_qconfig") | Default qconfig for quantizing weights only. |
| [`default_activation_only_qconfig`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.qconfig.default_activation_only_qconfig.html#torch.ao.quantization.qconfig.default_activation_only_qconfig "torch.ao.quantization.qconfig.default_activation_only_qconfig") | Default qconfig for quantizing activations only. |
| [`default_qat_qconfig_v2`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.qconfig.default_qat_qconfig_v2.html#torch.ao.quantization.qconfig.default_qat_qconfig_v2 "torch.ao.quantization.qconfig.default_qat_qconfig_v2") | Fused version of default\_qat\_config, has performance benefits. |

torch.ao.quantization.quantization\_mappings[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#module-torch.ao.quantization.quantization_mappings "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`get_default_compare_output_module_list`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantization_mappings.get_default_compare_output_module_list.html#torch.ao.quantization.quantization_mappings.get_default_compare_output_module_list "torch.ao.quantization.quantization_mappings.get_default_compare_output_module_list") | Get list of module class types that we will record output in numeric suite |
| [`get_default_dynamic_quant_module_mappings`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantization_mappings.get_default_dynamic_quant_module_mappings.html#torch.ao.quantization.quantization_mappings.get_default_dynamic_quant_module_mappings "torch.ao.quantization.quantization_mappings.get_default_dynamic_quant_module_mappings") | Get module mapping for post training dynamic quantization |
| [`get_default_dynamic_sparse_quant_module_mappings`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantization_mappings.get_default_dynamic_sparse_quant_module_mappings.html#torch.ao.quantization.quantization_mappings.get_default_dynamic_sparse_quant_module_mappings "torch.ao.quantization.quantization_mappings.get_default_dynamic_sparse_quant_module_mappings") | Get module mapping for post training dynamic sparse quantization |
| [`get_default_float_to_quantized_operator_mappings`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantization_mappings.get_default_float_to_quantized_operator_mappings.html#torch.ao.quantization.quantization_mappings.get_default_float_to_quantized_operator_mappings "torch.ao.quantization.quantization_mappings.get_default_float_to_quantized_operator_mappings") |     |
| [`get_default_qat_module_mappings`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantization_mappings.get_default_qat_module_mappings.html#torch.ao.quantization.quantization_mappings.get_default_qat_module_mappings "torch.ao.quantization.quantization_mappings.get_default_qat_module_mappings") | Get default module mapping for quantization aware training |
| [`get_default_qconfig_propagation_list`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantization_mappings.get_default_qconfig_propagation_list.html#torch.ao.quantization.quantization_mappings.get_default_qconfig_propagation_list "torch.ao.quantization.quantization_mappings.get_default_qconfig_propagation_list") | Get the default list of module types that we'll attach qconfig attribute to in prepare |
| [`get_default_static_quant_module_mappings`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantization_mappings.get_default_static_quant_module_mappings.html#torch.ao.quantization.quantization_mappings.get_default_static_quant_module_mappings "torch.ao.quantization.quantization_mappings.get_default_static_quant_module_mappings") | Get module mapping for post training static quantization |
| [`get_default_static_quant_reference_module_mappings`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantization_mappings.get_default_static_quant_reference_module_mappings.html#torch.ao.quantization.quantization_mappings.get_default_static_quant_reference_module_mappings "torch.ao.quantization.quantization_mappings.get_default_static_quant_reference_module_mappings") | Get reference module mapping for post training static quantization |
| [`get_default_static_sparse_quant_module_mappings`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantization_mappings.get_default_static_sparse_quant_module_mappings.html#torch.ao.quantization.quantization_mappings.get_default_static_sparse_quant_module_mappings "torch.ao.quantization.quantization_mappings.get_default_static_sparse_quant_module_mappings") | Get module mapping for post training static sparse quantization |
| [`get_dynamic_quant_module_class`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantization_mappings.get_dynamic_quant_module_class.html#torch.ao.quantization.quantization_mappings.get_dynamic_quant_module_class "torch.ao.quantization.quantization_mappings.get_dynamic_quant_module_class") | Get the dynamically quantized module class corresponding to the floating point module class |
| [`get_embedding_qat_module_mappings`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantization_mappings.get_embedding_qat_module_mappings.html#torch.ao.quantization.quantization_mappings.get_embedding_qat_module_mappings "torch.ao.quantization.quantization_mappings.get_embedding_qat_module_mappings") | Get module mapping for quantization aware training This is includes default values in addition to enabling qat for embeddings. |
| [`get_embedding_static_quant_module_mappings`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantization_mappings.get_embedding_static_quant_module_mappings.html#torch.ao.quantization.quantization_mappings.get_embedding_static_quant_module_mappings "torch.ao.quantization.quantization_mappings.get_embedding_static_quant_module_mappings") | Get module mapping, including mapping for embedding QAT |
| [`get_quantized_operator`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantization_mappings.get_quantized_operator.html#torch.ao.quantization.quantization_mappings.get_quantized_operator "torch.ao.quantization.quantization_mappings.get_quantized_operator") | Get the quantized operator corresponding to the float operator |
| [`get_static_quant_module_class`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantization_mappings.get_static_quant_module_class.html#torch.ao.quantization.quantization_mappings.get_static_quant_module_class "torch.ao.quantization.quantization_mappings.get_static_quant_module_class") | Get the statically quantized module class corresponding to the floating point module class |
| [`no_observer_set`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.quantization_mappings.no_observer_set.html#torch.ao.quantization.quantization_mappings.no_observer_set "torch.ao.quantization.quantization_mappings.no_observer_set") | These modules cannot have observers inserted by default. |

torch.ao.nn.intrinsic[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#module-torch.ao.nn.intrinsic "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

This module implements the combined (fused) modules conv + relu which can then be quantized.

|     |     |
| --- | --- |
| [`ConvReLU1d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.ConvReLU1d.html#torch.ao.nn.intrinsic.ConvReLU1d "torch.ao.nn.intrinsic.ConvReLU1d") | This is a sequential container which calls the Conv1d and ReLU modules. |
| [`ConvReLU2d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.ConvReLU2d.html#torch.ao.nn.intrinsic.ConvReLU2d "torch.ao.nn.intrinsic.ConvReLU2d") | This is a sequential container which calls the Conv2d and ReLU modules. |
| [`ConvReLU3d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.ConvReLU3d.html#torch.ao.nn.intrinsic.ConvReLU3d "torch.ao.nn.intrinsic.ConvReLU3d") | This is a sequential container which calls the Conv3d and ReLU modules. |
| [`LinearReLU`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.LinearReLU.html#torch.ao.nn.intrinsic.LinearReLU "torch.ao.nn.intrinsic.LinearReLU") | This is a sequential container which calls the Linear and ReLU modules. |
| [`ConvBn1d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.ConvBn1d.html#torch.ao.nn.intrinsic.ConvBn1d "torch.ao.nn.intrinsic.ConvBn1d") | This is a sequential container which calls the Conv 1d and Batch Norm 1d modules. |
| [`ConvBn2d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.ConvBn2d.html#torch.ao.nn.intrinsic.ConvBn2d "torch.ao.nn.intrinsic.ConvBn2d") | This is a sequential container which calls the Conv 2d and Batch Norm 2d modules. |
| [`ConvBn3d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.ConvBn3d.html#torch.ao.nn.intrinsic.ConvBn3d "torch.ao.nn.intrinsic.ConvBn3d") | This is a sequential container which calls the Conv 3d and Batch Norm 3d modules. |
| [`ConvBnReLU1d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.ConvBnReLU1d.html#torch.ao.nn.intrinsic.ConvBnReLU1d "torch.ao.nn.intrinsic.ConvBnReLU1d") | This is a sequential container which calls the Conv 1d, Batch Norm 1d, and ReLU modules. |
| [`ConvBnReLU2d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.ConvBnReLU2d.html#torch.ao.nn.intrinsic.ConvBnReLU2d "torch.ao.nn.intrinsic.ConvBnReLU2d") | This is a sequential container which calls the Conv 2d, Batch Norm 2d, and ReLU modules. |
| [`ConvBnReLU3d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.ConvBnReLU3d.html#torch.ao.nn.intrinsic.ConvBnReLU3d "torch.ao.nn.intrinsic.ConvBnReLU3d") | This is a sequential container which calls the Conv 3d, Batch Norm 3d, and ReLU modules. |
| [`BNReLU2d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.BNReLU2d.html#torch.ao.nn.intrinsic.BNReLU2d "torch.ao.nn.intrinsic.BNReLU2d") | This is a sequential container which calls the BatchNorm 2d and ReLU modules. |
| [`BNReLU3d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.BNReLU3d.html#torch.ao.nn.intrinsic.BNReLU3d "torch.ao.nn.intrinsic.BNReLU3d") | This is a sequential container which calls the BatchNorm 3d and ReLU modules. |

torch.ao.nn.intrinsic.qat[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#module-torch.ao.nn.intrinsic.qat "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

This module implements the versions of those fused operations needed for quantization aware training.

|     |     |
| --- | --- |
| [`LinearReLU`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.qat.LinearReLU.html#torch.ao.nn.intrinsic.qat.LinearReLU "torch.ao.nn.intrinsic.qat.LinearReLU") | A LinearReLU module fused from Linear and ReLU modules, attached with FakeQuantize modules for weight, used in quantization aware training. |
| [`ConvBn1d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.qat.ConvBn1d.html#torch.ao.nn.intrinsic.qat.ConvBn1d "torch.ao.nn.intrinsic.qat.ConvBn1d") | A ConvBn1d module is a module fused from Conv1d and BatchNorm1d, attached with FakeQuantize modules for weight, used in quantization aware training. |
| [`ConvBnReLU1d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.qat.ConvBnReLU1d.html#torch.ao.nn.intrinsic.qat.ConvBnReLU1d "torch.ao.nn.intrinsic.qat.ConvBnReLU1d") | A ConvBnReLU1d module is a module fused from Conv1d, BatchNorm1d and ReLU, attached with FakeQuantize modules for weight, used in quantization aware training. |
| [`ConvBn2d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.qat.ConvBn2d.html#torch.ao.nn.intrinsic.qat.ConvBn2d "torch.ao.nn.intrinsic.qat.ConvBn2d") | A ConvBn2d module is a module fused from Conv2d and BatchNorm2d, attached with FakeQuantize modules for weight, used in quantization aware training. |
| [`ConvBnReLU2d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.qat.ConvBnReLU2d.html#torch.ao.nn.intrinsic.qat.ConvBnReLU2d "torch.ao.nn.intrinsic.qat.ConvBnReLU2d") | A ConvBnReLU2d module is a module fused from Conv2d, BatchNorm2d and ReLU, attached with FakeQuantize modules for weight, used in quantization aware training. |
| [`ConvReLU2d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.qat.ConvReLU2d.html#torch.ao.nn.intrinsic.qat.ConvReLU2d "torch.ao.nn.intrinsic.qat.ConvReLU2d") | A ConvReLU2d module is a fused module of Conv2d and ReLU, attached with FakeQuantize modules for weight for quantization aware training. |
| [`ConvBn3d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.qat.ConvBn3d.html#torch.ao.nn.intrinsic.qat.ConvBn3d "torch.ao.nn.intrinsic.qat.ConvBn3d") | A ConvBn3d module is a module fused from Conv3d and BatchNorm3d, attached with FakeQuantize modules for weight, used in quantization aware training. |
| [`ConvBnReLU3d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.qat.ConvBnReLU3d.html#torch.ao.nn.intrinsic.qat.ConvBnReLU3d "torch.ao.nn.intrinsic.qat.ConvBnReLU3d") | A ConvBnReLU3d module is a module fused from Conv3d, BatchNorm3d and ReLU, attached with FakeQuantize modules for weight, used in quantization aware training. |
| [`ConvReLU3d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.qat.ConvReLU3d.html#torch.ao.nn.intrinsic.qat.ConvReLU3d "torch.ao.nn.intrinsic.qat.ConvReLU3d") | A ConvReLU3d module is a fused module of Conv3d and ReLU, attached with FakeQuantize modules for weight for quantization aware training. |
| [`update_bn_stats`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.qat.update_bn_stats.html#torch.ao.nn.intrinsic.qat.update_bn_stats "torch.ao.nn.intrinsic.qat.update_bn_stats") |     |
| [`freeze_bn_stats`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.qat.freeze_bn_stats.html#torch.ao.nn.intrinsic.qat.freeze_bn_stats "torch.ao.nn.intrinsic.qat.freeze_bn_stats") |     |

torch.ao.nn.intrinsic.quantized[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#module-torch.ao.nn.intrinsic.quantized "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------

This module implements the quantized implementations of fused operations like conv + relu. No BatchNorm variants as it’s usually folded into convolution for inference.

|     |     |
| --- | --- |
| [`BNReLU2d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.quantized.BNReLU2d.html#torch.ao.nn.intrinsic.quantized.BNReLU2d "torch.ao.nn.intrinsic.quantized.BNReLU2d") | A BNReLU2d module is a fused module of BatchNorm2d and ReLU |
| [`BNReLU3d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.quantized.BNReLU3d.html#torch.ao.nn.intrinsic.quantized.BNReLU3d "torch.ao.nn.intrinsic.quantized.BNReLU3d") | A BNReLU3d module is a fused module of BatchNorm3d and ReLU |
| [`ConvReLU1d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.quantized.ConvReLU1d.html#torch.ao.nn.intrinsic.quantized.ConvReLU1d "torch.ao.nn.intrinsic.quantized.ConvReLU1d") | A ConvReLU1d module is a fused module of Conv1d and ReLU |
| [`ConvReLU2d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.quantized.ConvReLU2d.html#torch.ao.nn.intrinsic.quantized.ConvReLU2d "torch.ao.nn.intrinsic.quantized.ConvReLU2d") | A ConvReLU2d module is a fused module of Conv2d and ReLU |
| [`ConvReLU3d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.quantized.ConvReLU3d.html#torch.ao.nn.intrinsic.quantized.ConvReLU3d "torch.ao.nn.intrinsic.quantized.ConvReLU3d") | A ConvReLU3d module is a fused module of Conv3d and ReLU |
| [`LinearReLU`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.quantized.LinearReLU.html#torch.ao.nn.intrinsic.quantized.LinearReLU "torch.ao.nn.intrinsic.quantized.LinearReLU") | A LinearReLU module fused from Linear and ReLU modules |

torch.ao.nn.intrinsic.quantized.dynamic[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#module-torch.ao.nn.intrinsic.quantized.dynamic "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This module implements the quantized dynamic implementations of fused operations like linear + relu.

|     |     |
| --- | --- |
| [`LinearReLU`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.intrinsic.quantized.dynamic.LinearReLU.html#torch.ao.nn.intrinsic.quantized.dynamic.LinearReLU "torch.ao.nn.intrinsic.quantized.dynamic.LinearReLU") | A LinearReLU module fused from Linear and ReLU modules that can be used for dynamic quantization. |

torch.ao.nn.qat[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#module-torch.ao.nn.qat "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

This module implements versions of the key nn modules **Conv2d()** and **Linear()** which run in FP32 but with rounding applied to simulate the effect of INT8 quantization.

|     |     |
| --- | --- |
| [`Conv2d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.qat.Conv2d.html#torch.ao.nn.qat.Conv2d "torch.ao.nn.qat.Conv2d") | A Conv2d module attached with FakeQuantize modules for weight, used for quantization aware training. |
| [`Conv3d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.qat.Conv3d.html#torch.ao.nn.qat.Conv3d "torch.ao.nn.qat.Conv3d") | A Conv3d module attached with FakeQuantize modules for weight, used for quantization aware training. |
| [`Linear`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.qat.Linear.html#torch.ao.nn.qat.Linear "torch.ao.nn.qat.Linear") | A linear module attached with FakeQuantize modules for weight, used for quantization aware training. |

torch.ao.nn.qat.dynamic[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#module-torch.ao.nn.qat.dynamic "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

This module implements versions of the key nn modules such as **Linear()** which run in FP32 but with rounding applied to simulate the effect of INT8 quantization and will be dynamically quantized during inference.

|     |     |
| --- | --- |
| [`Linear`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.qat.dynamic.Linear.html#torch.ao.nn.qat.dynamic.Linear "torch.ao.nn.qat.dynamic.Linear") | A linear module attached with FakeQuantize modules for weight, used for dynamic quantization aware training. |

torch.ao.nn.quantized[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#module-torch.ao.nn.quantized.modules "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

This module implements the quantized versions of the nn layers such as `~torch.nn.Conv2d` and `torch.nn.ReLU`.

|     |     |
| --- | --- |
| [`ReLU6`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.ReLU6.html#torch.ao.nn.quantized.ReLU6 "torch.ao.nn.quantized.ReLU6") | Applies the element-wise function: |
| [`Hardswish`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.Hardswish.html#torch.ao.nn.quantized.Hardswish "torch.ao.nn.quantized.Hardswish") | This is the quantized version of [`Hardswish`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Hardswish.html#torch.nn.Hardswish "torch.nn.Hardswish")<br>. |
| [`ELU`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.ELU.html#torch.ao.nn.quantized.ELU "torch.ao.nn.quantized.ELU") | This is the quantized equivalent of [`ELU`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.ELU.html#torch.nn.ELU "torch.nn.ELU")<br>. |
| [`LeakyReLU`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.LeakyReLU.html#torch.ao.nn.quantized.LeakyReLU "torch.ao.nn.quantized.LeakyReLU") | This is the quantized equivalent of [`LeakyReLU`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.LeakyReLU.html#torch.nn.LeakyReLU "torch.nn.LeakyReLU")<br>. |
| [`Sigmoid`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.Sigmoid.html#torch.ao.nn.quantized.Sigmoid "torch.ao.nn.quantized.Sigmoid") | This is the quantized equivalent of [`Sigmoid`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Sigmoid.html#torch.nn.Sigmoid "torch.nn.Sigmoid")<br>. |
| [`BatchNorm2d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.BatchNorm2d.html#torch.ao.nn.quantized.BatchNorm2d "torch.ao.nn.quantized.BatchNorm2d") | This is the quantized version of [`BatchNorm2d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.BatchNorm2d.html#torch.nn.BatchNorm2d "torch.nn.BatchNorm2d")<br>. |
| [`BatchNorm3d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.BatchNorm3d.html#torch.ao.nn.quantized.BatchNorm3d "torch.ao.nn.quantized.BatchNorm3d") | This is the quantized version of [`BatchNorm3d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.BatchNorm3d.html#torch.nn.BatchNorm3d "torch.nn.BatchNorm3d")<br>. |
| [`Conv1d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.Conv1d.html#torch.ao.nn.quantized.Conv1d "torch.ao.nn.quantized.Conv1d") | Applies a 1D convolution over a quantized input signal composed of several quantized input planes. |
| [`Conv2d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.Conv2d.html#torch.ao.nn.quantized.Conv2d "torch.ao.nn.quantized.Conv2d") | Applies a 2D convolution over a quantized input signal composed of several quantized input planes. |
| [`Conv3d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.Conv3d.html#torch.ao.nn.quantized.Conv3d "torch.ao.nn.quantized.Conv3d") | Applies a 3D convolution over a quantized input signal composed of several quantized input planes. |
| [`ConvTranspose1d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.ConvTranspose1d.html#torch.ao.nn.quantized.ConvTranspose1d "torch.ao.nn.quantized.ConvTranspose1d") | Applies a 1D transposed convolution operator over an input image composed of several input planes. |
| [`ConvTranspose2d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.ConvTranspose2d.html#torch.ao.nn.quantized.ConvTranspose2d "torch.ao.nn.quantized.ConvTranspose2d") | Applies a 2D transposed convolution operator over an input image composed of several input planes. |
| [`ConvTranspose3d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.ConvTranspose3d.html#torch.ao.nn.quantized.ConvTranspose3d "torch.ao.nn.quantized.ConvTranspose3d") | Applies a 3D transposed convolution operator over an input image composed of several input planes. |
| [`Embedding`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.Embedding.html#torch.ao.nn.quantized.Embedding "torch.ao.nn.quantized.Embedding") | A quantized Embedding module with quantized packed weights as inputs. |
| [`EmbeddingBag`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.EmbeddingBag.html#torch.ao.nn.quantized.EmbeddingBag "torch.ao.nn.quantized.EmbeddingBag") | A quantized EmbeddingBag module with quantized packed weights as inputs. |
| [`FloatFunctional`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.FloatFunctional.html#torch.ao.nn.quantized.FloatFunctional "torch.ao.nn.quantized.FloatFunctional") | State collector class for float operations. |
| [`FXFloatFunctional`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.FXFloatFunctional.html#torch.ao.nn.quantized.FXFloatFunctional "torch.ao.nn.quantized.FXFloatFunctional") | module to replace FloatFunctional module before FX graph mode quantization, since activation\_post\_process will be inserted in top level module directly |
| [`QFunctional`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.QFunctional.html#torch.ao.nn.quantized.QFunctional "torch.ao.nn.quantized.QFunctional") | Wrapper class for quantized operations. |
| [`Linear`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.Linear.html#torch.ao.nn.quantized.Linear "torch.ao.nn.quantized.Linear") | A quantized linear module with quantized tensor as inputs and outputs. |
| [`LayerNorm`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.LayerNorm.html#torch.ao.nn.quantized.LayerNorm "torch.ao.nn.quantized.LayerNorm") | This is the quantized version of [`LayerNorm`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.LayerNorm.html#torch.nn.LayerNorm "torch.nn.LayerNorm")<br>. |
| [`GroupNorm`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.GroupNorm.html#torch.ao.nn.quantized.GroupNorm "torch.ao.nn.quantized.GroupNorm") | This is the quantized version of [`GroupNorm`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.GroupNorm.html#torch.nn.GroupNorm "torch.nn.GroupNorm")<br>. |
| [`InstanceNorm1d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.InstanceNorm1d.html#torch.ao.nn.quantized.InstanceNorm1d "torch.ao.nn.quantized.InstanceNorm1d") | This is the quantized version of [`InstanceNorm1d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.InstanceNorm1d.html#torch.nn.InstanceNorm1d "torch.nn.InstanceNorm1d")<br>. |
| [`InstanceNorm2d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.InstanceNorm2d.html#torch.ao.nn.quantized.InstanceNorm2d "torch.ao.nn.quantized.InstanceNorm2d") | This is the quantized version of [`InstanceNorm2d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.InstanceNorm2d.html#torch.nn.InstanceNorm2d "torch.nn.InstanceNorm2d")<br>. |
| [`InstanceNorm3d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.InstanceNorm3d.html#torch.ao.nn.quantized.InstanceNorm3d "torch.ao.nn.quantized.InstanceNorm3d") | This is the quantized version of [`InstanceNorm3d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.InstanceNorm3d.html#torch.nn.InstanceNorm3d "torch.nn.InstanceNorm3d")<br>. |

torch.ao.nn.quantized.functional[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#module-torch.ao.nn.quantized.functional "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Functional interface (quantized).

This module implements the quantized versions of the functional layers such as ~torch.nn.functional.conv2d and torch.nn.functional.relu. Note:  torch.nn.functional.relu~torch.nn.functional.relu torch.nn.functional.relu supports quantized inputs.

|     |     |
| --- | --- |
| [`avg_pool2d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.functional.avg_pool2d.html#torch.ao.nn.quantized.functional.avg_pool2d "torch.ao.nn.quantized.functional.avg_pool2d") | Applies 2D average-pooling operation in kH×kWkH \\times kWkH×kW regions by step size sH×sWsH \\times sWsH×sW steps. |
| [`avg_pool3d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.functional.avg_pool3d.html#torch.ao.nn.quantized.functional.avg_pool3d "torch.ao.nn.quantized.functional.avg_pool3d") | Applies 3D average-pooling operation in kD×kH×kWkD \\times kH \\times kWkD×kH×kW regions by step size sD×sH×sWsD \\times sH \\times sWsD×sH×sW steps. |
| [`adaptive_avg_pool2d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.functional.adaptive_avg_pool2d.html#torch.ao.nn.quantized.functional.adaptive_avg_pool2d "torch.ao.nn.quantized.functional.adaptive_avg_pool2d") | Applies a 2D adaptive average pooling over a quantized input signal composed of several quantized input planes. |
| [`adaptive_avg_pool3d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.functional.adaptive_avg_pool3d.html#torch.ao.nn.quantized.functional.adaptive_avg_pool3d "torch.ao.nn.quantized.functional.adaptive_avg_pool3d") | Applies a 3D adaptive average pooling over a quantized input signal composed of several quantized input planes. |
| [`conv1d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.functional.conv1d.html#torch.ao.nn.quantized.functional.conv1d "torch.ao.nn.quantized.functional.conv1d") | Applies a 1D convolution over a quantized 1D input composed of several input planes. |
| [`conv2d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.functional.conv2d.html#torch.ao.nn.quantized.functional.conv2d "torch.ao.nn.quantized.functional.conv2d") | Applies a 2D convolution over a quantized 2D input composed of several input planes. |
| [`conv3d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.functional.conv3d.html#torch.ao.nn.quantized.functional.conv3d "torch.ao.nn.quantized.functional.conv3d") | Applies a 3D convolution over a quantized 3D input composed of several input planes. |
| [`interpolate`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.functional.interpolate.html#torch.ao.nn.quantized.functional.interpolate "torch.ao.nn.quantized.functional.interpolate") | Down/up samples the input to either the given `size` or the given `scale_factor` |
| [`linear`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.functional.linear.html#torch.ao.nn.quantized.functional.linear "torch.ao.nn.quantized.functional.linear") | Applies a linear transformation to the incoming quantized data: y\=xAT+by = xA^T + by\=xAT+b. |
| [`max_pool1d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.functional.max_pool1d.html#torch.ao.nn.quantized.functional.max_pool1d "torch.ao.nn.quantized.functional.max_pool1d") | Applies a 1D max pooling over a quantized input signal composed of several quantized input planes. |
| [`max_pool2d`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.functional.max_pool2d.html#torch.ao.nn.quantized.functional.max_pool2d "torch.ao.nn.quantized.functional.max_pool2d") | Applies a 2D max pooling over a quantized input signal composed of several quantized input planes. |
| [`celu`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.functional.celu.html#torch.ao.nn.quantized.functional.celu "torch.ao.nn.quantized.functional.celu") | Applies the quantized CELU function element-wise. |
| [`leaky_relu`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.functional.leaky_relu.html#torch.ao.nn.quantized.functional.leaky_relu "torch.ao.nn.quantized.functional.leaky_relu") | Quantized version of the. |
| [`hardtanh`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.functional.hardtanh.html#torch.ao.nn.quantized.functional.hardtanh "torch.ao.nn.quantized.functional.hardtanh") | This is the quantized version of [`hardtanh()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.hardtanh.html#torch.nn.functional.hardtanh "torch.nn.functional.hardtanh")<br>. |
| [`hardswish`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.functional.hardswish.html#torch.ao.nn.quantized.functional.hardswish "torch.ao.nn.quantized.functional.hardswish") | This is the quantized version of [`hardswish()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.hardswish.html#torch.nn.functional.hardswish "torch.nn.functional.hardswish")<br>. |
| [`threshold`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.functional.threshold.html#torch.ao.nn.quantized.functional.threshold "torch.ao.nn.quantized.functional.threshold") | Applies the quantized version of the threshold function element-wise: |
| [`elu`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.functional.elu.html#torch.ao.nn.quantized.functional.elu "torch.ao.nn.quantized.functional.elu") | This is the quantized version of [`elu()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.elu.html#torch.nn.functional.elu "torch.nn.functional.elu")<br>. |
| [`hardsigmoid`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.functional.hardsigmoid.html#torch.ao.nn.quantized.functional.hardsigmoid "torch.ao.nn.quantized.functional.hardsigmoid") | This is the quantized version of [`hardsigmoid()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.hardsigmoid.html#torch.nn.functional.hardsigmoid "torch.nn.functional.hardsigmoid")<br>. |
| [`clamp`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.functional.clamp.html#torch.ao.nn.quantized.functional.clamp "torch.ao.nn.quantized.functional.clamp") | float(input, min\_, max\_) -> Tensor |
| [`upsample`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.functional.upsample.html#torch.ao.nn.quantized.functional.upsample "torch.ao.nn.quantized.functional.upsample") | Upsamples the input to either the given `size` or the given `scale_factor` |
| [`upsample_bilinear`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.functional.upsample_bilinear.html#torch.ao.nn.quantized.functional.upsample_bilinear "torch.ao.nn.quantized.functional.upsample_bilinear") | Upsamples the input, using bilinear upsampling. |
| [`upsample_nearest`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.functional.upsample_nearest.html#torch.ao.nn.quantized.functional.upsample_nearest "torch.ao.nn.quantized.functional.upsample_nearest") | Upsamples the input, using nearest neighbours' pixel values. |

torch.ao.nn.quantizable[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#torch-ao-nn-quantizable "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

This module implements the quantizable versions of some of the nn layers. These modules can be used in conjunction with the custom module mechanism, by providing the `custom_module_config` argument to both prepare and convert.

|     |     |
| --- | --- |
| [`LSTM`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantizable.LSTM.html#torch.ao.nn.quantizable.LSTM "torch.ao.nn.quantizable.LSTM") | A quantizable long short-term memory (LSTM). |
| [`MultiheadAttention`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantizable.MultiheadAttention.html#torch.ao.nn.quantizable.MultiheadAttention "torch.ao.nn.quantizable.MultiheadAttention") |     |

torch.ao.nn.quantized.dynamic[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#module-torch.ao.nn.quantized.dynamic "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

Dynamically quantized [`Linear`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Linear.html#torch.nn.Linear "torch.nn.Linear")
, [`LSTM`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.LSTM.html#torch.nn.LSTM "torch.nn.LSTM")
, [`LSTMCell`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.LSTMCell.html#torch.nn.LSTMCell "torch.nn.LSTMCell")
, [`GRUCell`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.GRUCell.html#torch.nn.GRUCell "torch.nn.GRUCell")
, and [`RNNCell`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.RNNCell.html#torch.nn.RNNCell "torch.nn.RNNCell")
.

|     |     |
| --- | --- |
| [`Linear`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.dynamic.Linear.html#torch.ao.nn.quantized.dynamic.Linear "torch.ao.nn.quantized.dynamic.Linear") | A dynamic quantized linear module with floating point tensor as inputs and outputs. |
| [`LSTM`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.dynamic.LSTM.html#torch.ao.nn.quantized.dynamic.LSTM "torch.ao.nn.quantized.dynamic.LSTM") | A dynamic quantized LSTM module with floating point tensor as inputs and outputs. |
| [`GRU`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.dynamic.GRU.html#torch.ao.nn.quantized.dynamic.GRU "torch.ao.nn.quantized.dynamic.GRU") | Applies a multi-layer gated recurrent unit (GRU) RNN to an input sequence. |
| [`RNNCell`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.dynamic.RNNCell.html#torch.ao.nn.quantized.dynamic.RNNCell "torch.ao.nn.quantized.dynamic.RNNCell") | An Elman RNN cell with tanh or ReLU non-linearity. |
| [`LSTMCell`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.dynamic.LSTMCell.html#torch.ao.nn.quantized.dynamic.LSTMCell "torch.ao.nn.quantized.dynamic.LSTMCell") | A long short-term memory (LSTM) cell. |
| [`GRUCell`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.nn.quantized.dynamic.GRUCell.html#torch.ao.nn.quantized.dynamic.GRUCell "torch.ao.nn.quantized.dynamic.GRUCell") | A gated recurrent unit (GRU) cell |

Quantized dtypes and quantization schemes[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#quantized-dtypes-and-quantization-schemes "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Note that operator implementations currently only support per channel quantization for weights of the **conv** and **linear** operators. Furthermore, the input data is mapped linearly to the quantized data and vice versa as follows:

> Quantization:Qout\=clamp(xinput/s+z,Qmin,Qmax)Dequantization:xout\=(Qinput−z)∗s\\begin{aligned} \\text{Quantization:}&\\\\ &Q\_\\text{out} = \\text{clamp}(x\_\\text{input}/s+z, Q\_\\text{min}, Q\_\\text{max})\\\\ \\text{Dequantization:}&\\\\ &x\_\\text{out} = (Q\_\\text{input}-z)\*s \\end{aligned}Quantization:Dequantization:​Qout​\=clamp(xinput​/s+z,Qmin​,Qmax​)xout​\=(Qinput​−z)∗s​

where clamp(.)\\text{clamp}(.)clamp(.) is the same as [`clamp()`](https://docs.pytorch.org/docs/2.15/generated/torch.clamp.html#torch.clamp "torch.clamp")
 while the scale sss and zero point zzz are then computed as described in [`MinMaxObserver`](https://docs.pytorch.org/docs/2.15/generated/torch.ao.quantization.observer.MinMaxObserver.html#torch.ao.quantization.observer.MinMaxObserver "torch.ao.quantization.observer.MinMaxObserver")
, specifically:

> if Symmetric:s\=2max⁡(∣xmin∣,xmax)/(Qmax−Qmin)z\={0if dtype is qint8128otherwiseOtherwise:s\=(xmax−xmin)/(Qmax−Qmin)z\=Qmin−round(xmin/s)\\begin{aligned} \\text{if Symmetric:}&\\\\ &s = 2 \\max(|x\_\\text{min}|, x\_\\text{max}) / \\left( Q\_\\text{max} - Q\_\\text{min} \\right) \\\\ &z = \\begin{cases} 0 & \\text{if dtype is qint8} \\\\ 128 & \\text{otherwise} \\end{cases}\\\\ \\text{Otherwise:}&\\\\ &s = \\left( x\_\\text{max} - x\_\\text{min} \\right ) / \\left( Q\_\\text{max} - Q\_\\text{min} \\right ) \\\\ &z = Q\_\\text{min} - \\text{round}(x\_\\text{min} / s) \\end{aligned}if Symmetric:Otherwise:​s\=2max(∣xmin​∣,xmax​)/(Qmax​−Qmin​)z\={0128​if dtype is qint8otherwise​s\=(xmax​−xmin​)/(Qmax​−Qmin​)z\=Qmin​−round(xmin​/s)​

where :math:`[x_\text{min}, x_\text{max}]` denotes the range of the input data while :math:`Q_\text{min}` and :math:`Q_\text{max}` are respectively the minimum and maximum values of the quantized dtype.

Note that the choice of :math:`s` and :math:`z` implies that zero is represented with no quantization error whenever zero is within the range of the input data or symmetric quantization is being used.

Additional data types and quantization schemes can be implemented through the `custom operator mechanism <https://pytorch.org/tutorials/advanced/torch_script_custom_ops.html>`\_.

*   `torch.qscheme` — Type to describe the quantization scheme of a tensor. Supported types:
    
    *   `torch.per_tensor_affine` — per tensor, asymmetric
        
    *   `torch.per_channel_affine` — per channel, asymmetric
        
    *   `torch.per_tensor_symmetric` — per tensor, symmetric
        
    *   `torch.per_channel_symmetric` — per channel, symmetric
        
*   `torch.dtype` — Type to describe the data. Supported types:
    
    *   `torch.quint8` — 8-bit unsigned integer
        
    *   `torch.qint8` — 8-bit signed integer
        
    *   `torch.qint32` — 32-bit signed integer
        

QAT Modules.

This package is in the process of being deprecated. Please, use torch.ao.nn.qat.modules instead.

QAT Dynamic Modules.

This package is in the process of being deprecated. Please, use torch.ao.nn.qat.dynamic instead.

This file is in the process of migration to torch/ao/quantization, and is kept here for compatibility while the migration process is ongoing. If you are adding a new entry/functionality, please, add it to the appropriate files under torch/ao/quantization/fx/, while adding an import statement here.

QAT Dynamic Modules.

This package is in the process of being deprecated. Please, use torch.ao.nn.qat.dynamic instead.

Quantized Modules.

Note::

The torch.nn.quantized namespace is in the process of being deprecated. Please, use torch.ao.nn.quantized instead.

Quantized Dynamic Modules.

This file is in the process of migration to torch/ao/nn/quantized/dynamic, and is kept here for compatibility while the migration process is ongoing. If you are adding a new entry/functionality, please, add it to the appropriate file under the torch/ao/nn/quantized/dynamic, while adding an import statement here.

torch.quantization.default\_eval\_fn(_model_, _calib\_data_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/quantization/__init__.py#L14)
[#](https://docs.pytorch.org/docs/2.15/quantization-support.html#torch.quantization.default_eval_fn "Link to this definition")

Default evaluation function takes a torch.utils.data.Dataset or a list of input Tensors and run the model on the dataset

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/quantization-support.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/quantization-support.md.txt)

PyTorch Libraries

*   [ExecuTorch](https://docs.pytorch.org/executorch)
    
*   [Helion](https://docs.pytorch.org/helion)
    
*   [torchao](https://docs.pytorch.org/ao)
    
*   [kineto](https://github.com/pytorch/kineto)
    
*   [torchtitan](https://github.com/pytorch/torchtitan)
    
*   [TorchRL](https://docs.pytorch.org/rl)
    
*   [torchvision](https://docs.pytorch.org/vision)
    
*   [torchaudio](https://docs.pytorch.org/audio)
    
*   [tensordict](https://docs.pytorch.org/tensordict)
    
*   [PyTorch on XLA Devices](https://docs.pytorch.org/xla)
    

Docs
----

Access comprehensive developer documentation for PyTorch

[View Docs](https://docs.pytorch.org/docs/stable/index.html)

Tutorials
---------

Get in-depth tutorials for beginners and advanced developers

[View Tutorials](https://docs.pytorch.org/tutorials)

Resources
---------

Find development resources and get your questions answered

[View Resources](https://pytorch.org/resources)

To analyze traffic and optimize your experience, we serve cookies on this site. By clicking or navigating, you agree to allow our usage of cookies. As the current maintainers of this site, Facebook’s Cookies Policy applies. Learn more, including about available controls: [Cookies Policy](https://opensource.fb.com/legal/cookie-policy)
.

|     |     |
| --- | --- |
|     |     |

|     |     |
| --- | --- |
|     |     |