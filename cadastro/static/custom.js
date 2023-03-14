var SPMaskBehavior = function (val) {
    return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
  },
  spOptions = {
    onKeyPress: function(val, e, field, options) {
        field.mask(SPMaskBehavior.apply({}, arguments), options);
      }
  };
    
  django.jQuery(document).ready(function(){
    django.jQuery(".mask-cpf").mask("000.000.000-00", {placeholder:"000.000.000-00"});            
    django.jQuery(".mask-celular").mask(SPMaskBehavior, spOptions);
    django.jQuery(".mask-telefone_res").mask(SPMaskBehavior, spOptions);
    django.jQuery(".mask-nascimento").mask("00/00/0000", {placeholder:"__/__/____"});
    django.jQuery(".mask-numero").mask("0000000000", {placeholder:"0000000000"});
    django.jQuery(".mask-cep").mask("00000-000", {placeholder:"00000-000"});
    django.jQuery(".mask-sus").mask("000000000000000", {placeholder:"000000000000000"});
    django.jQuery(".mask-rg").mask("00000000", {placeholder:"00000000"});
});
      