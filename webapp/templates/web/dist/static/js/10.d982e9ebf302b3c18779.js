webpackJsonp([10],{KMh2:function(e,t){},h7M0:function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var n=a("Dd8w"),r=a.n(n),o=a("D4TX"),l=a("gyMJ"),s=a("NYxO"),u={components:{Crumbs:o.a},data:function(){return{tableData:[]}},methods:r()({},Object(s.b)(["TOSAST_STATE"]),{getData:function(){var e=this,t=JSON.parse(localStorage.getItem("userInfo"));Object(l.q)({token:t.token,username:t.user}).then(function(t){t.errcode?(e.TOSAST_STATE({text:t.msg}),2==t.errcode&&setTimeout(function(){localStorage.removeItem("userInfo"),e.$router.push("/login")},1e3)):e.tableData=t.data.list})},deleteRow:function(e,t){var a=this,n=JSON.parse(localStorage.getItem("userInfo"));Object(l.d)({token:n.token,username:n.user,id:t.id}).then(function(t){a.TOSAST_STATE({text:t.msg}),t.errcode?2==t.errcode&&setTimeout(function(){localStorage.removeItem("userInfo"),a.$router.push("/login")},1e3):a.tableData.splice(e,1)})}}),created:function(){this.getData()}},c={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("Crumbs",{attrs:{crumbs1:"模板",crumbs2:"模板列表"}}),e._v(" "),a("el-table",{attrs:{data:e.tableData}},[a("el-table-column",{attrs:{type:"index"}}),e._v(" "),a("el-table-column",{attrs:{prop:"name",label:"名称"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("router-link",{attrs:{to:/template_list/+t.row.id}},[e._v(e._s(t.row.name))])]}}])}),e._v(" "),a("el-table-column",{attrs:{prop:"remarks",label:"备注"}}),e._v(" "),a("el-table-column",{attrs:{label:"操作"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("el-button",{attrs:{type:"text",size:"small"},on:{click:function(a){e.deleteRow(t.$index,t.row)}}},[e._v("删除")])]}}])})],1)],1)},staticRenderFns:[]};var i=a("VU/8")(u,c,!1,function(e){a("KMh2")},"data-v-2d2d656c",null);t.default=i.exports}});
//# sourceMappingURL=10.d982e9ebf302b3c18779.js.map