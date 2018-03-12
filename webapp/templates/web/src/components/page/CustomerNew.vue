<template>
  <div>
    <Crumbs crumbs1="客户" crumbs2="添加客户"></Crumbs>
    <div class="form-box">
      <el-form label-width="80px">
        <el-form-item label="姓名">
          <el-input v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item label="电话号码">
          <el-input v-model="form.num"></el-input>
        </el-form-item>
        <el-form-item label="住址">
          <el-input v-model="form.addNum"></el-input>
        </el-form-item>
        <el-form-item label="备注">
          <el-input type="textarea" v-model="form.remarks"></el-input>
        </el-form-item>
        <el-form-item label="选择模板">
          <el-radio-group v-model="checkedTem">
            <el-radio v-for="(item,index) in templateList" :key="index" :label="item.name"></el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="货物列表" v-if="checkedTem">
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
  import {templateList} from "../../api"

  export default {
    components: {
      Crumbs
    },
    data(){
      return {
        form: {
          name: '',
          tel: '',
          remarks: '',
          address: ''
        },
        templateList: [],
        checkedStocks: [],
        checkedTem: ''
      }
    },
    computed: {
      currentTemGoods() {
        let currentTem = this.templateList.find(item => item.name == this.checkedTem)
        if(currentTem) {
          this.checkedStocks = currentTem.goods
          return currentTem.goods
        }
        return []
      }
    },
    methods: {
      onSubmit() {
        console.log("submit")
      }
    },
    created() {
      templateList().then(res => {
        if(!res.errcode) {
          this.templateList = res.data.list
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
  .min-height {
    height: 200px;
    border: 1px solid #eee;
    padding: 0 10px;
    overflow: auto;
  }
</style>
