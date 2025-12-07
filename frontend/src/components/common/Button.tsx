import { ButtonHTMLAttributes, ReactNode } from 'react'
import { clsx } from 'clsx'

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'accent' | 'danger'
  size?: 'sm' | 'md' | 'lg'
  children: ReactNode
}

export default function Button({ variant = 'primary', size = 'md', className, children, ...props }: ButtonProps) {
  return (
    <button className={clsx('btn-retro', { 'btn-retro-sm': size === 'sm', 'btn-retro-lg': size === 'lg', 'btn-retro-accent': variant === 'accent', 'btn-retro-danger': variant === 'danger' }, className)} {...props}>
      {children}
    </button>
  )
}
