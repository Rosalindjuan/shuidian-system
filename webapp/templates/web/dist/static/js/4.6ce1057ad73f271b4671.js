webpackJsonp([4],{GF4k:function(e,r,s){"use strict";Object.defineProperty(r,"__esModule",{value:!0});var t=s("Dd8w"),o=s.n(t),a=s("gyMJ"),l=s("NYxO"),n={data:function(){return{ruleForm:{username:"",password:""},rules:{username:[{required:!0,message:"请输入用户名",trigger:"blur"}],password:[{required:!0,message:"请输入密码",trigger:"blur"},{min:6,max:12,message:"长度在 6 到 12 个字符",trigger:"blur"}]}}},methods:o()({},Object(l.b)(["TOSAST_STATE","GET_USERINFO","REWRITE_USERINFO"]),{submitForm:function(e){var r=this;this.$refs[e].validate(function(e){if(!e)return console.log("error submit!!"),!1;Object(a.s)({username:r.ruleForm.username,password:r.ruleForm.password}).then(function(e){e.errcode?r.TOSAST_STATE({text:e.msg}):(r.REWRITE_USERINFO(e.data),console.log(e),r.$router.push("/stock_list"))})})}})},u={render:function(){var e=this,r=e.$createElement,s=e._self._c||r;return s("div",{staticClass:"login-wrap"},[s("div",{staticClass:"ms-title"},[e._v("后台管理系统")]),e._v(" "),s("div",{staticClass:"ms-login"},[s("el-form",{ref:"ruleForm",staticClass:"demo-ruleForm",attrs:{model:e.ruleForm,rules:e.rules,"label-width":"0px"}},[s("el-form-item",{attrs:{prop:"username"}},[s("el-input",{attrs:{placeholder:"username"},model:{value:e.ruleForm.username,callback:function(r){e.$set(e.ruleForm,"username",r)},expression:"ruleForm.username"}})],1),e._v(" "),s("el-form-item",{attrs:{prop:"password"}},[s("el-input",{attrs:{type:"password",placeholder:"password"},nativeOn:{keyup:function(r){if(!("button"in r)&&e._k(r.keyCode,"enter",13,r.key))return null;e.submitForm("ruleForm")}},model:{value:e.ruleForm.password,callback:function(r){e.$set(e.ruleForm,"password",r)},expression:"ruleForm.password"}})],1),e._v(" "),s("div",{staticClass:"login-btn"},[s("el-button",{attrs:{type:"primary"},on:{click:function(r){e.submitForm("ruleForm")}}},[e._v("登录")])],1),e._v(" "),s("p",{staticStyle:{"font-size":"12px","line-height":"30px",color:"#999"}},[e._v("Tips : 用户名和密码随便填。")])],1)],1)])},staticRenderFns:[]};var i=s("VU/8")(n,u,!1,function(e){s("dMqx")},"data-v-78112876",null);r.default=i.exports},dMqx:function(e,r){}});
//# sourceMappingURL=4.6ce1057ad73f271b4671.js.map