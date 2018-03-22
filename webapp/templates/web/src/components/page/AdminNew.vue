<template>
  <div>
    <Crumbs crumbs1="管理员" crumbs2="添加管理员"></Crumbs>
    <div class="form-box">
      <el-form :model="form" :rules="rules" ref="rulesform" label-width="90px">
        <el-form-item prop="user" label="用户名:">
          <el-col :span="10">
            <el-input v-model="form.user" placeholder="用户名"></el-input>
          </el-col>
          <!--<el-col class="center-right" :span="4" required>真实姓名：</el-col>-->
          <el-col :span="14">
            <el-form-item prop="name" label="真实姓名:">
              <el-input v-model="form.name" placeholder="姓名"></el-input>
            </el-form-item>
          </el-col>
        </el-form-item>
        <el-form-item label="密码:" prop="password">
          <el-col :span="10">
            <el-input type="password" v-model="form.password" placeholder="密码"></el-input>
          </el-col>
          <!--<el-col class="center-right" :span="4">确认密码：</el-col>-->
          <el-col :span="14">
            <el-form-item label="确认密码: " prop="surePsd">
              <el-input type="password" v-model="form.surePsd" placeholder="确认密码"></el-input>
            </el-form-item>
          </el-col>
        </el-form-item>
        <el-form-item label="电话号码:" prop="tel">
          <el-col :span="10">
            <!--<el-input v-model="form.tel"></el-input>-->
            <el-input v-model="form.tel" placeholder="电话号码"></el-input>
          </el-col>
        </el-form-item>
        <br>
        <el-form-item label="部门:">
          <el-col :span="10">
            <el-form-item prop="department">
              <el-input v-model="form.department" placeholder="部门"></el-input>
            </el-form-item>
          </el-col>
          <el-col class="center-right" :span="4">职位：</el-col>
          <el-col :span="10">
            <el-form-item prop="position">
              <el-input v-model="form.position" placeholder="职位"></el-input>
            </el-form-item>
          </el-col>
        </el-form-item>
        <el-form-item label="电子邮箱:">
          <el-col :span="10">
            <el-form-item prop="email">
              <el-input v-model="form.email" placeholder="电子邮箱"></el-input>
            </el-form-item>
          </el-col>
          <el-col class="center-right" :span="4">微信：</el-col>
          <el-col :span="10">
            <el-form-item prop="wechat">
              <el-input v-model="form.wechat" placeholder="微信"></el-input>
            </el-form-item>
          </el-col>
        </el-form-item>
        <el-form-item label="QQ:" prop="qq">
          <el-col :span="10">
            <el-input type="tel" v-model="form.qq" placeholder="qq"></el-input>
          </el-col>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm('rulesform')">提交</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
  import Crumbs from "../common/Crumbs.vue"
  import {mapMutations, mapState} from 'vuex'
  import {newAdmin} from "../../api"


  export default {
    components: {
      Crumbs
    },
    data() {
      var validatePass = (rule, value, callback) => {
        if (value !== this.form.password) {
          callback(new Error('两次输入密码不一致!'));
        } else {
          callback();
        }
      }
      return {
        form: {
          user: '',
          name: '',
          password: '',
          surePsd: '',
          tel: null,
          department: '',
          position: '',
          email: '',
          wechat: '',
          qq: ''
        },
        rules: {
          user: [{required: true, message: '请输入用户名', trigger: 'blur'}],
          name: [{required: true, message: '请输入姓名', trigger: 'blur'}],
          password: [
            {required: true, message: '请输入密码', trigger: 'blur'},
            {min: 6, max: 12, message: '长度在 6 到 12 个字符', trigger: 'blur'}
          ],
          surePsd: [
            {required: true, message: '请输入确认密码', trigger: 'blur'},
            {min: 6, max: 12, message: '长度在 6 到 12 个字符', trigger: 'blur'},
            {validator: validatePass, trigger: 'blur'}

          ],
          tel: [
            {required: true, message: '请输入电话号码', trigger: 'blur'},
            {pattern: /^\d{6,11}$/, message: '长度在 6 到 11 个数字',}
          ],
        }
      }
    },
    methods: {
      ...mapMutations(['TOSAST_STATE']),
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            console.log('submit', this.form)
            let userInfo = JSON.parse(localStorage.getItem('userInfo'));

            newAdmin({token: userInfo.token, username: userInfo.user, ...this.form}).then(res => {
              console.log(res)
              this.TOSAST_STATE({text: res.msg})


              if (!res.errcode) {
                this.form = {
                  user: '',
                  name: '',
                  password: '',
                  surePsd: '',
                  tel: null,
                  department: '',
                  position: '',
                  email: '',
                  wechat: '',
                  qq: ''
                }
              }else{
                if(res.errcode == 2) {
                  setTimeout(() => {
                    localStorage.removeItem('userInfo')
                    this.$router.push('/login');
                  }, 1000)
                }
              }
            })
          } else {
            console.log('error submit!!');
            return false;
          }
        });

      }
    },
    created() {
    }
  }
</script>

<style scoped>
</style>
