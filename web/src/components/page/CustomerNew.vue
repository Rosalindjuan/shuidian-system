<template>
  <div>
    <Crumbs crumbs1="客户" crumbs2="添加客户"></Crumbs>
    <div class="form-box">
      <el-form ref="form" :model="form" label-width="80px">
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
          <el-radio-group v-model="form.resource">
            <el-radio label="步步高"></el-radio>
            <el-radio label="小天才"></el-radio>
            <el-radio label="imoo"></el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="多选框">
          <el-checkbox-group v-model="form.type">
            <el-checkbox label="步步高1" name="type"></el-checkbox>
            <el-checkbox label="小天才2" name="type"></el-checkbox>
            <el-checkbox label="imoo3" name="type"></el-checkbox>
            <el-checkbox label="步步高4" name="type"></el-checkbox>
            <el-checkbox label="小天才5" name="type"></el-checkbox>
            <el-checkbox label="imoo6" name="type"></el-checkbox>
            <el-checkbox label="步步高7" name="type"></el-checkbox>
            <el-checkbox label="小天才8" name="type"></el-checkbox>
            <el-checkbox label="imoo9" name="type"></el-checkbox>
            <el-checkbox label="步步高10" name="type"></el-checkbox>
            <el-checkbox label="小天才11" name="type"></el-checkbox>
            <el-checkbox label="imoo12" name="type"></el-checkbox>
            <el-checkbox label="步步高13" name="type"></el-checkbox>
            <el-checkbox label="小天才14" name="type"></el-checkbox>
            <el-checkbox label="imoo15" name="type"></el-checkbox>
            <el-checkbox label="步步高16" name="type"></el-checkbox>
            <el-checkbox label="小天才17" name="type"></el-checkbox>
            <el-checkbox label="imoo18" name="type"></el-checkbox>
            <el-checkbox label="步步高19" name="type"></el-checkbox>
            <el-checkbox label="小天才20" name="type"></el-checkbox>
            <el-checkbox label="imoo21" name="type"></el-checkbox>
            <el-checkbox label="步步高22" name="type"></el-checkbox>
            <el-checkbox label="小天才23" name="type"></el-checkbox>
            <el-checkbox label="imoo24" name="type"></el-checkbox>
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
  export default {
    components: {
      Crumbs
    },
    data(){
      return {
        form: {
          type: ['步步高'],
          resource: '小天才',
        }
      }
    },
    methods: {
      onSubmit() {
        console.log("submit")
      }
    }
  }
</script>

<style scoped>
  .el-checkbox:nth-child(5n+1) {
    margin-left: 0;
  }
</style>
