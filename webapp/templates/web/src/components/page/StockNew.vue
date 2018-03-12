<template>
  <div>
    <Crumbs crumbs1="库存" :crumbs2="crumbs2"></Crumbs>
    <div class="form-box">
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="名称">
          <el-input v-model="form.name" :disabled="readonly"></el-input>
        </el-form-item>
        <el-form-item label="数量">
          <el-input v-model="form.num" :disabled="readonly"></el-input>
        </el-form-item>
        <el-form-item label="添加数量">
          <el-input v-model="form.addNum"></el-input>
        </el-form-item>
        <el-form-item label="单位">
          <el-input v-model="form.unit"></el-input>
        </el-form-item>
        <el-form-item label="进价">
          <el-input v-model="form.opening_price"></el-input>
        </el-form-item>
        <el-form-item label="单价">
          <el-input v-model="form.price"></el-input>
        </el-form-item>
        <el-form-item label="备注">
          <el-input type="textarea" v-model="form.remarks"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">提交</el-button>
          <!--<el-button>取消</el-button>-->
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
  import Crumbs from "../common/Crumbs.vue"
  import {newStock, updateStock, getStock} from "../../api"

  export default {
    components: {
      Crumbs
    },
    data() {
      return {
        crumbs2: '新建库存',
        readonly: false,
        form: {
          name: '',
          num: 0,
          addNum: 0,
          unit: '',
          opening_price: 0,
          price: 0,
          remarks: '',
        }
      }
    },
    methods: {
      onSubmit() {
        let newNum = parseInt(this.form.num) + parseInt(this.form.addNum)
        let params = {
          name: this.form.name,
          num: newNum,
          unit: this.form.unit,
          opening_price: this.form.opening_price,
          price: this.form.price,
          remarks: this.form.remarks
        }

        if (this.readonly) {
          updateStock(params).then(res => {
            if (!res.errcode) {
              alert('已修改成功')
              this.form.addNum = '0'
              this.form.num = newNum
            } else {
              alert(res.msg)
            }
          })
        } else {
          if (this.form.name.trim()) {
            newStock(params).then(res => {
              if (!res.errcode) {
                alert('添加成功')
                this.form = {
                  name: '',
                  num: 0,
                  addNum: 0,
                  unit: '',
                  opening_price: 0,
                  price: 0,
                  remarks: '',
                }
              } else {
                alert(res.msg)
              }
            })
          } else {
            alert('请填写名称')
          }
        }
      },
      setDetail() {
        if (this.$route.params.id) {
          this.crumbs2 = '物品详情'
          this.readonly = true
          let param = {params: {id: this.$route.params.id}}
          getStock(param).then(res => {
            if (!res.errcode) {
              this.form = res.data
              this.form.addNum = 0
            }
          })
        } else {
          this.crumbs2 = '新建库存'
          this.readonly = false
          this.form = {
            name: '',
            num: 0,
            addNum: 0,
            unit: '',
            opening_price: 0,
            price: 0,
            remarks: '',
          }
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
