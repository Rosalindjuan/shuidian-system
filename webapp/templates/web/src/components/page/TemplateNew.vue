<template>
  <div>
    <Crumbs crumbs1="模板" :crumbs2="crumbs2"></Crumbs>
    <div class="form-box">
      <p>选择需要的货物添加至模板</p>
      <el-form>
        <el-form-item label="模板名称">
          <el-input v-model="name" :disabled="readonly"></el-input>
        </el-form-item>
        <el-form-item label="备注">
          <el-input v-model="remarks"></el-input>
        </el-form-item>
        <el-form-item>
          <el-checkbox :indeterminate="isIndeterminate" v-model="checkAll" @change="handleCheckAllChange">全选
          </el-checkbox>
        </el-form-item>
        <el-form-item>
          <el-checkbox-group v-model="checkedStocks" @change="handleCheckedChange">
            <el-checkbox v-for="stock in stocks" :label="stock" :key="stock">{{stock}}</el-checkbox>
          </el-checkbox-group>
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
  import {getStocks, newTemplate, temGoodsList, updateTemplate} from "../../api"

  export default {
    components: {
      Crumbs
    },
    data() {
      return {
        crumbs2: '新建模板',
        name: '',
        remarks: '',
        readonly: false,
        stocks: [],
        checkedStocks: [],
        checkAll: false,
        isIndeterminate: true
      }
    },
    methods: {
      // 是否全选
      handleCheckAllChange(val) {
        this.checkedStocks = val ? this.stocks : [];
        this.isIndeterminate = false;
      },

      handleCheckedChange(value) {
        let checkedCount = value.length;
        this.checkAll = checkedCount === this.stocks.length;
        this.isIndeterminate = checkedCount > 0 && checkedCount < this.stocks.length;
      },
      // 判断是否输入名称
      checkname() {
        if (!this.name.trim()) {
          alert('请输入名称')
          return false
        }
        return true
      },
      // 判断是否选择货物
      checkStock() {
        if (this.checkedStocks.length < 1) {
          alert('请选择货物')
          return false
        }
        return true
      },
      // 提交
      onSubmit() {
//        console.log(this.checkedStocks, 'submit')
        if (this.checkStock() && this.checkname()) {
          let param = {name: this.name, remarks: this.remarks, goods: this.checkedStocks}
          if (this.readonly) {
            updateTemplate(param).then(res => {
              alert(res.msg)
//              console.log('修改模板',res)
            })
          } else {
            newTemplate(param).then(res => {
//              console.log(res)
              alert(res.msg)
              if (!res.errcode) {
                this.name = ''
                this.remarks = ''
                this.checkedStocks = this.stocks
                this.isIndeterminate = false;
                this.checkAll = true
              }
            })
          }
        }
      },
      // 判断arr2里面的元素是否和arr1一样
      judgeEequal(arr1, arr2) {
        let arr = []
        if (arr1.length == arr2.length) {
          arr1.forEach(item => {
            arr2.forEach(item2 => {
              if (item == item2) {
                arr.push(item)
              }
            })
          })
          return arr.length == arr1.length ? true : false
        } else {
          return false
        }
      },
      setDetail() {
        if (this.$route.params.id) {
          this.crumbs2 = '模板详情'
          this.readonly = true
          let param = {id: this.$route.params.id}
          console.log('模板详情')
          temGoodsList(param).then(res => {
            console.log(res)
            if (!res.errcode) {
              this.name = res.data.name
              this.remarks = res.data.remarks
              this.checkedStocks = res.data.list
              let ifAll = this.judgeEequal(this.stocks, this.checkedStocks)
              this.isIndeterminate = this.checkedStocks.length > 0 && !ifAll
              this.checkAll = ifAll
            }
          })
        } else {
          console.log('新建模板')
          this.crumbs2 = '新建模板'
          this.name = ''
          this.remarks = ''
          this.readonly = false
          this.isIndeterminate = false;
          this.checkedStocks = this.stocks
          this.checkAll = true
        }
      }
    },
    created() {
      getStocks().then(res => {
        if (!res.errcode) {
          this.stocks = res.data.list
          this.setDetail()
        }
      })


    },
    watch: {
      '$route'() {
        this.setDetail()
      }
    }
  }
</script>

<style scoped>
  .el-checkbox {
    margin-right: 30px;
    margin-left: 0;
  }
</style>
