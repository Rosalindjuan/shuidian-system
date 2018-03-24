<template>
  <div>
    <Crumbs crumbs1="客户" crumbs2="添加客户"></Crumbs>
    <div class="form-box">
      <el-form label-width="100px" :model="form" :rules="rules" ref="rulesform">
        <el-form-item label="姓名" prop="name">
          <el-input v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item label="电话号码" prop="tel">
          <el-input v-model="form.tel"></el-input>
        </el-form-item>
        <el-form-item label="住址" prop="address">
          <el-input v-model="form.address"></el-input>
        </el-form-item>
        <el-form-item label="备注" prop="remarks">
          <el-input type="textarea" v-model="form.remarks"></el-input>
        </el-form-item>
        <el-form-item label="选择模板" prop="checkedTem">
          <el-radio-group v-model="form.checkedTem">
            <el-radio v-for="(item,index) in templateList" :key="index" :label="item.name"></el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="物料列表" v-if="form.checkedTem">
          <p class="red">请选择客户所需的物料</p>
          <el-checkbox-group v-model="checkedStocks" class="min-height">
            <el-checkbox v-for="(goods,i) in currentTemGoods" :key="i" :label="goods" name="type"></el-checkbox>
          </el-checkbox-group>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">提交</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
  import Crumbs from "../common/Crumbs.vue"
  import {templateList, newCustomer} from "../../api"
  import {mapMutations, mapState} from 'vuex'

  export default {
    components: {
      Crumbs
    },
    data() {
      return {
        form: {
          name: '',
          tel: '',
          remarks: '',
          address: '',
          checkedTem: '',
        },
        checkedStocks: [],
        templateList: [],
        rules: {
          name: [{required: true, message: '请输入客户姓名', trigger: 'blur'}],
          tel: [{required: true, message: '请输入电话号码', trigger: 'blur'}],
          address: [{required: true, message: '请输入客户住址', trigger: 'blur'}],
          checkedTem: [{required: true, message: '请选择一个模板', trigger: 'blur, change'}],
        }
      }
    },
    computed: {
      currentTemGoods() {
        let currentTem = this.templateList.find(item => item.name == this.form.checkedTem)
        if (currentTem) {
          this.checkedStocks = currentTem.goods
          return currentTem.goods
        }
        return []
      }
    },
    methods: {
      ...mapMutations(['TOSAST_STATE']),
      onSubmit() {
        this.$refs['rulesform'].validate((valid) => {
          if (valid) {
            if (this.checkedStocks.length > 0) {
              let userInfo = JSON.parse(localStorage.getItem('userInfo'));
              let params = {
                token: userInfo.token,
                username: userInfo.user,
                form: this.form,
                checkedStocks: this.checkedStocks
              }
              newCustomer(params).then(res => {
                this.TOSAST_STATE({text: res.msg})
                if (!res.errcode) {
                  this.form = {
                    name: '',
                    tel: '',
                    remarks: '',
                    address: '',
                    checkedTem: '',
                  }
                  this.checkedStocks = []
                }
              })
            } else {
              this.TOSAST_STATE({text: '请选择客户所需的物料'})
            }
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      }
    },
    created() {
      let userInfo = JSON.parse(localStorage.getItem('userInfo'));
      templateList({token: userInfo.token, username: userInfo.user}).then(res => {
        if (!res.errcode) {
          this.templateList = res.data.list
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
  .el-checkbox {
    margin-left: 0;
    margin-right: 30px;
  }
  .el-radio {
    margin-left: 0;
    margin-right: 30px;
    margin-bottom: 15px;
  }
  .min-height {
    height: 200px;
    border: 1px solid #eee;
    padding: 0 10px;
    overflow: auto;
  }
</style>
