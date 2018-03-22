<template>
  <div>
    <Crumbs crumbs1="管理员" crumbs2="管理员详情"></Crumbs>
    <div class="form-box">
      <!--<h2 class="page-title">管理员信息</h2>-->
      <el-row>
        <el-col :span="4">用户名：</el-col>
        <el-col :span="8">{{admin.username ? admin.username : '----'}}</el-col>
        <el-col :span="4">真实姓名：</el-col>
        <el-col :span="8">{{admin.name ? admin.name : '----'}}</el-col>
        <el-col :span="4">电话号码：</el-col>
        <el-col :span="8">{{admin.tel ? admin.tel : '----'}}</el-col>
      </el-row>
      <el-row>
        <el-col :span="4">部门：</el-col>
        <el-col :span="8">{{admin.department ? admin.department : '----'}}</el-col>
        <el-col :span="4">职位：</el-col>
        <el-col :span="8">{{admin.position ? admin.position : '----'}}</el-col>
        <el-col :span="4">电子邮箱：</el-col>
        <el-col :span="8">{{admin.email ? admin.email : '----'}}</el-col>
        <el-col :span="4">微信：</el-col>
        <el-col :span="8">{{admin.wechat ? admin.wechat : '----'}}</el-col>
        <el-col :span="4">QQ：</el-col>
        <el-col :span="8">{{admin.qq ? admin.qq : '----'}}</el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
  import Crumbs from "../common/Crumbs.vue"
  import {getAdmin} from "../../api"


  export default {
    components: {
      Crumbs
    },
    data() {
      return {
        admin: {}
      }
    },
    created() {
      let userInfo = JSON.parse(localStorage.getItem('userInfo'));
      getAdmin({params: {id: this.$route.params.id, token: userInfo.token, username: userInfo.user}}).then(res => {
        if (!res.errcode) {
          this.admin = res.data
        } else {
          this.TOSAST_STATE({text: res.msg})
          if (res.errcode == 2) {
            setTimeout(() => {
              localStorage.removeItem('userInfo')
              this.$router.push('/login');
            }, 1000)
          }
        }
      })
    }
  }
</script>

<style scoped>
  .el-col {
    margin-bottom: 20px;
  }

  .el-row {
    margin: 40px 0;
  }
</style>
