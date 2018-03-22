<template>
  <div>
    <Crumbs crumbs1="客户" crumbs2="客户详情"></Crumbs>
    <div class="plugins-tips">客户基本信息</div>
    <div class="form-box">
      <el-form label-width="100px" :model="form" :rules="rules" ref="rulesform">
        <el-form-item label="姓名">{{form.name}}</el-form-item>
        <el-form-item label="电话号码" prop="tel">
          <el-input v-model="form.tel"></el-input>
        </el-form-item>
        <el-form-item label="住址" prop="address">
          <el-input v-model="form.address"></el-input>
        </el-form-item>
        <el-form-item label="备注" prop="remarks">
          <el-input type="textarea" v-model="form.remarks"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmitCus">保存</el-button>
        </el-form-item>
      </el-form>
    </div>
    <br>
    <div class="plugins-tips">还款信息</div>
    <ul class="repay-info form-box">
      <li class="amount">应还款总额： <span>{{currentAmount}}</span>元</li>
      <li>
        <ul>
          <li>付款金额(￥)</li>
          <li>付款时间</li>
        </ul>
        <ul v-for="(repay, i) in repayList" :key="i">
          <li>{{repay.amount}}</li>
          <li>{{repay.time}}</li>
        </ul>
        <ul>
          <li>
            <el-input v-model="repay.repayMoney" placeholder="输入付款金额"></el-input>
          </li>
          <li>
            <el-date-picker type="date" placeholder="选择日期"
                            v-model="repay.repayTime"
                            value-format="yyyy-MM-dd" style="width: 100%;"></el-date-picker>
          </li>
        </ul>
        <ul>
          <li class="add-btn">
            <el-button type="primary" @click="addRepay">添加</el-button>
          </li>
        </ul>

      </li>
    </ul>
    <div class="plugins-tips">客户用到的物料列表</div>
    <div class="form-box">
      <el-form>
        <el-form-item>
          <el-table :data="goodsList">
            <el-table-column type="index"></el-table-column>
            <el-table-column prop="stock_name" label="名称"></el-table-column>
            <el-table-column prop="stock_num" label="数量" width="100">
              <template slot-scope="scope">
                <el-input v-model="scope.row.stock_num"></el-input>
              </template>
            </el-table-column>
            <el-table-column prop="stock_price" label="单价" width="100">
              <template slot-scope="scope">
                <el-input v-model="scope.row.stock_price"></el-input>
              </template>
            </el-table-column>
            <el-table-column label="金额" prop="stock_amount">
              <template slot-scope="scope">{{perAmount}}
                {{scope.row.stock_num * scope.row.stock_price}}
              </template>
            </el-table-column>
          </el-table>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmitGoods">保存</el-button>
          <el-button type="text" @click="dialogVisible = true">添加物料</el-button>
          <!--<el-button type="primary" v-popover:popover>添加使用物料</el-button>-->
        </el-form-item>
      </el-form>

    </div>

    <!--<el-dialog title="提示" :visible.sync="dialogVisible" width="30%">-->
    <!--<span>这里是添加物料的信息</span>-->
    <!--<span slot="footer" class="dialog-footer">-->
    <!--<el-button @click="dialogVisible = false">取 消</el-button>-->
    <!--<el-button type="primary" @click="dialogVisible = false">确 定</el-button>-->
    <!--</span>-->
    <!--</el-dialog>-->
  </div>
</template>

<script>
  import Crumbs from "../common/Crumbs.vue"
  import {getCustomer, addCusRepay, updateCustomer, updateCusGoods} from "../../api"
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
          address: ''
        },
        dialogVisible: false,
        rules: {
          name: [{required: true, message: '请输入客户姓名', trigger: 'blur'}],
          tel: [{required: true, message: '请输入电话号码', trigger: 'blur'}],
          address: [{required: true, message: '请输入客户住址', trigger: 'blur'}],
        },
        goodsList: [],
        repay: {
          repayMoney: '',
          repayTime: ''
        },
        repayList: [],
      }
    },
    computed: {
      // 总金额
      currentAmount() {
        let amount = 0
        this.goodsList.map(item => {
          amount += item.stock_price * item.stock_num
        })
        return amount
      },
      perAmount() {
        this.goodsList.map(item => {
          item.stock_price = +item.stock_price
          item.stock_num = +item.stock_num
          return item.stock_amount = item.stock_price * item.stock_num
        })
      }
    },
    methods: {
      ...mapMutations(['TOSAST_STATE']),

      addGoods() {

      },
      // 修改客户信息
      onSubmitCus() {
        this.$refs['rulesform'].validate((valid) => {
          if (valid) {
            let userInfo = JSON.parse(localStorage.getItem('userInfo'));
            let params = {token: userInfo.token, username: userInfo.user, id: this.$route.params.id, form: this.form}
            updateCustomer(params).then(res => {
              this.TOSAST_STATE({text: res.msg})
              if (res.errcode == 2) {
                setTimeout(() => {
                  localStorage.removeItem('userInfo')
                  this.$router.push('/login');
                }, 1000)
              }
            })
          } else {
            return false;
          }
        });
      },
      // 用料提交
      onSubmitGoods() {
        let userInfo = JSON.parse(localStorage.getItem('userInfo'));
        let params = {
          token: userInfo.token,
          username: userInfo.user,
          id: this.$route.params.id,
          goodsList: this.goodsList
        }
        updateCusGoods(params).then(res => {
          this.TOSAST_STATE({text: res.msg})
          if (res.errcode == 2) {
            setTimeout(() => {
              localStorage.removeItem('userInfo')
              this.$router.push('/login');
            }, 1000)
          }
        })
      },
      judgeRepayMoney() {
        if (this.repay.repayMoney) {
          return true
        } else {
          this.TOSAST_STATE({text: '请输入付款金额'})
          return false
        }
      },
      judgeRepayTime() {
        if (this.repay.repayTime) {
          return true
        } else {
          this.TOSAST_STATE({text: '请选择付款日期'})
          return false
        }
      },
      // 添加付款信息
      addRepay() {
        if (this.judgeRepayMoney() && this.judgeRepayTime()) {
          console.log(this.judgeRepayMoney && this.judgeRepayTime)
          let userInfo = JSON.parse(localStorage.getItem('userInfo'));
          let param = {
            token: userInfo.token,
            username: userInfo.user,
            id: this.$route.params.id,
            amount: this.repay.repayMoney,
            time: this.repay.repayTime
          }
          addCusRepay(param).then(res => {
//            console.log('添加付款',res)
            this.TOSAST_STATE({text: res.msg})
            if (!res.errcode) {
              // 添加付款信息 提交
              this.repayList.push({amount: this.repay.repayMoney, time: this.repay.repayTime})
              this.repay.repayMoney = ''
              this.repay.repayTime = ''
            } else {
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
    },
    created() {
      let userInfo = JSON.parse(localStorage.getItem('userInfo'));
      let param = {params: {id: this.$route.params.id, token: userInfo.token, username: userInfo.user}}
      getCustomer(param).then(res => {
        console.log(res)
        if (!res.errcode) {
          this.form = res.data.info
          this.goodsList = res.data.goods_list
          this.repayList = res.data.repay_list
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
  ul, li {
    list-style: none;
  }

  .repay-info {
    display: flex;
    align-items: center;
    border: 1px solid #ebeef5;
    margin-top: 20px;
    margin-bottom: 20px;
  }

  .amount {
    width: 200px;
  }

  .repay-info li {
    padding: 10px;
    width: 200px;
  }

  .repay-info > li:last-child {
    padding: 0;
    width: 400px;
  }

  .repay-info > li > ul {
    width: 100%;
    display: flex;
    border-bottom: 1px solid #ebeef5;
    text-align: center;
  }

  .repay-info > li > ul li {
    border-left: 1px solid #ebeef5;
  }

  .repay-info > li > ul:last-child {
    border-bottom: none;
  }

  .repay-info > li > ul li.add-btn {
    width: 100%;
  }

  .add-btn button {
    display: block;
    margin: 0 auto;
  }
</style>
