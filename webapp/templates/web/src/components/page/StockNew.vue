<template>
  <div>
    <Crumbs crumbs1="库存" :crumbs2="crumbs2"></Crumbs>
    <div class="form-box">
      <el-form :model="form" :rules="rules" ref="rulesform" label-width="80px">
        <el-form-item label="名称" prop="name">
          <el-input v-model="form.name" :disabled="readonly"></el-input>
        </el-form-item>
        <!--<el-form-item label="数量" prop="num">-->
          <!--<el-input v-model="form.num" :disabled="readonly"></el-input>-->
        <!--</el-form-item>-->
        <!--<el-form-item label="添加数量" prop="addNum">-->
          <!--<el-input v-model="form.addNum"></el-input>-->
        <!--</el-form-item>-->
        <el-form-item label="单位" prop="unit">
          <el-input v-model="form.unit"></el-input>
        </el-form-item>
        <!--<el-form-item label="进价" prop="opening_price">-->
          <!--<el-input v-model="form.opening_price"></el-input>-->
        <!--</el-form-item>-->
        <el-form-item label="单价" prop="price">
          <el-input v-model="form.price"></el-input>
        </el-form-item>
        <el-form-item label="备注" prop="remarks">
          <el-input type="textarea" v-model="form.remarks"></el-input>
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
  import {newStock, updateStock, getStock} from "../../api"
  import {mapMutations, mapState} from 'vuex'


  export default {
    components: {
      Crumbs
    },
    data() {
      return {
        crumbs2: '新建库存',
        readonly: false,
        form: {name: '', num: 0, addNum: 0, unit: '个', opening_price: 0, price: 0, remarks: ''},
        rules: {
          name: [{required: true, message: '请输入物料名称', trigger: 'blur'}],
          unit: [{required: true, message: '请输入物料单位', trigger: 'blur'}],
        }
      }
    },
    methods: {
      ...mapMutations(['TOSAST_STATE']),
      // 提交
      onSubmit() {
        let newNum = parseInt(this.form.num) + parseInt(this.form.addNum)
        let userInfo = JSON.parse(localStorage.getItem('userInfo'));
        let params = {
          username: userInfo.user,
          token: userInfo.token,
          name: this.form.name,
          num: newNum,
          unit: this.form.unit,
          opening_price: this.form.opening_price,
          price: this.form.price,
          remarks: this.form.remarks
        }
        this.$refs['rulesform'].validate((valid) => {
          if (valid) {
            if (this.readonly) { // 更新物料信息
              updateStock(params).then(res => {
                this.TOSAST_STATE({text: res.msg})
                if (!res.errcode) {
                  this.form.addNum = '0'
                  this.form.num = newNum
                } else if (res.errcode == 2){
                  this.$router.push('/login');
                }
              })
            } else { // 创建物料
              newStock(params).then(res => {
                this.TOSAST_STATE({text: res.msg})
                if (!res.errcode) {
                  this.form = {name: '', num: 0, addNum: 0, unit: '个', opening_price: 0, price: 0, remarks: ''}
                } else if (res.errcode == 2){
                  this.$router.push('/login');
                }
              })
            }
          } else {
//            console.log('error submit!!');
            return false;
          }
        });


      },
      setDetail() {
        if (this.$route.params.id) {
          this.crumbs2 = '物品详情'
          this.readonly = true
          let userInfo = JSON.parse(localStorage.getItem('userInfo'));
          let param = {params: {id: this.$route.params.id,token: userInfo.token,username:userInfo.user}}
          getStock(param).then(res => {
            console.log(res)
            if (!res.errcode) {
              this.form = res.data
              this.form.addNum = 0
            }else{
              this.TOSAST_STATE({text: res.msg})
              if(res.errcode == 2) {
                setTimeout(() => {
                  localStorage.removeItem('userInfo')
                  this.$router.push('/login');
                }, 1000)
              }
            }
          })
        } else {
          this.crumbs2 = '新建库存'
          this.readonly = false
          this.form = {name: '', num: 0, addNum: 0, unit: '个', opening_price: 0, price: 0, remarks: ''}
        }
      }
    },
    created() {
      this.setDetail()
    },
    watch: {
      '$route'() {
        this.setDetail()
      }
    }
  }
</script>

<style scoped>
  .form-box {
    padding-top: 20px;
  }
</style>
