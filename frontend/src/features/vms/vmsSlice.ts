import { createSlice, PayloadAction } from '@reduxjs/toolkit'

interface VM {
  id: string
  name: string
  status: 'running' | 'stopped' | 'error'
  ip: string
}

interface VMsState {
  vms: VM[]
  loading: boolean
}

const initialState: VMsState = {
  vms: [],
  loading: false,
}

const vmsSlice = createSlice({
  name: 'vms',
  initialState,
  reducers: {
    setVMs: (state, action: PayloadAction<VM[]>) => {
      state.vms = action.payload
    },
    updateVMStatus: (state, action: PayloadAction<{ id: string; status: string }>) => {
      const vm = state.vms.find(v => v.id === action.payload.id)
      if (vm) {
        vm.status = action.payload.status as any
      }
    },
  },
})

export const { setVMs, updateVMStatus } = vmsSlice.actions
export default vmsSlice.reducer
