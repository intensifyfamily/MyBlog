<template>
  <div>
    <el-card>
      <div style="padding: 40px 50px">
        <el-row>
          <el-col>添加待办事项</el-col>
        </el-row>
        <el-divider><i class="el-icon-mobile-phone"></i></el-divider>
        <el-row>
          <el-col>
            <el-form>
              <el-form-item label="title">
                <el-input v-model="addInfo.title"></el-input>
              </el-form-item>
              <el-form-item label="content">
                <el-input v-model="addInfo.content" type="textarea"></el-input>
              </el-form-item>
              <el-button type="primary" @click="add">添加</el-button>
            </el-form>
          </el-col>
        </el-row>
      </div>
    </el-card>
    <el-card>
      <div style="padding: 40px 50px">
        <el-row>
          <el-col>待办事项列表</el-col>
        </el-row>
        <el-divider><i class="el-icon-mobile-phone"></i></el-divider>
        <span v-if="toDoCount.length === 0" style="color: #808080;font-size: 12px;">暂无待办事项...</span>
        <el-row class="list_item" v-for="item in toDoCount" :key="item.id">
          <el-col :span="2">
            <el-checkbox label="已完成" v-model="item.is_done" border size="small" @change="setStatusChanged(item)"></el-checkbox>
          </el-col>
          <el-col :span="22">
              <el-alert
                :title="item.title"
                type="warning"
                effect="dark"
                :description="item.content"
                @close="setDelete(item.id)">
              </el-alert>
          </el-col>
        </el-row>
      </div>
    </el-card>
    <el-card>
      <div style="padding: 40px 50px">
        <el-row>
          <el-col>已办事项列表</el-col>
        </el-row>
        <el-divider><i class="el-icon-mobile-phone"></i></el-divider>
        <span v-if="doneCount.length === 0" style="color: #808080;font-size: 12px;">暂无已办事项...</span>
        <el-row class="list_item" v-for="item in doneCount" :key="item.id">
          <el-col :span="2">
            <el-checkbox label="未完成" v-model="item.is_done" border size="small" @change="setStatusChanged(item, 1)"></el-checkbox>
          </el-col>
          <el-col :span="22">
              <el-alert
                :title="item.title"
                type="success"
                effect="dark"
                :description="item.content"
                @close="setDelete(item.id)">
              </el-alert>
          </el-col>
        </el-row>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  data () {
    return {
      addInfo: {
        title: '',
        content: ''
      },
      toDoCount: [],
      doneCount: []
    }
  },
  created () {
    this.getList()
  },
  methods: {
    async getList () {
      this.toDoCount = []
      this.doneCount = []
      const { data: res } = await this.$http.get('todo')
      if (res.data.meta.status !== 200) {
        return this.$message.error('获取失败！')
      }
      res.data.results.forEach((item) => {
        if (item.is_done === 0) {
          this.toDoCount.push(item)
        } else {
          this.doneCount.push(item)
        }
      })
    },
    async add () {
      if (!this.addInfo.title || !this.addInfo.content) {
        return this.$message.info('请输入title和content！')
      }
      const { data: res } = await this.$http.post('todo', this.addInfo)
      if (res.data.meta.status !== 200) {
        return this.$message.error('添加失败！')
      }
      this.$message.success('添加成功！')
      this.addInfo = {
        title: '',
        content: ''
      }
      this.getList()
    },
    async setStatusChanged (item, check = null) {
      item.is_done = item.is_done === true ? 1 : 0
      const { data: res } = await this.$http.put('todo', item)
      if (res.data.meta.status !== 200) {
        return this.$message.error('更新失败！')
      }
      this.$message.success('更新成功！')
      item.is_done = item.is_done === 1
      if (check) item.is_done = !item.is_done
    },
    async setDelete (itemId) {
      const { data: res } = await this.$http.get(`todo/${itemId}`)
      if (res.data.meta.status !== 200) {
        return this.$message.error('删除失败！')
      }
      this.$message.info('删除成功！')
      this.getList()
    }
  }
}
</script>

<style lang="less" scoped>
.el-card {
  margin-bottom: 15px;
}
.list_item {
  margin-bottom: 20px;
}
</style>
